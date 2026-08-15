"""Validate a runtime-neutral deliberation decision packet."""

import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath, PureWindowsPath


MAX_PACKET_BYTES = 1024 * 1024
IDENTIFIER = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
MODES = {"decide", "review", "synthesize"}
OUTCOMES = {"substantive", "procedural"}
ASSESSMENTS = {"meets", "fails", "unknown"}
GATE_KINDS = {"threshold", "test", "artifact", "state"}
EVIDENCE_QUALITIES = {"strong", "moderate", "weak", "insufficient"}
INDEPENDENCE_LEVELS = {"L0", "L1", "L2", "imported"}
REQUIRED_FIELDS = {
    "schema_version", "mode", "outcome", "answer", "criteria", "options",
    "selected_option_id", "supported_facts", "inferences", "assumptions",
    "disputed_claims", "decision_basis", "information_gaps", "next_action",
    "risks", "change_conditions", "confidence", "material_dissent", "coverage",
}


@dataclass(frozen=True, order=True)
class ValidationError:
    code: str
    pointer: str
    message: str


def add_error(errors, code, pointer, message):
    errors.append(ValidationError(code, pointer, message))


def nonempty_text(value):
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def valid_identifier(value):
    return isinstance(value, str) and IDENTIFIER.fullmatch(value) is not None


def safe_source(value):
    if not nonempty_text(value) or value.startswith("~"):
        return False
    posix = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if posix.is_absolute() or windows.is_absolute() or windows.drive:
        return False
    return ".." not in posix.parts and ".." not in windows.parts


def normalized_claim(value):
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = "".join(
        character if character.isalnum() else " " for character in normalized
    )
    return " ".join(normalized.split())


def is_string_list(value):
    return isinstance(value, list) and all(nonempty_text(item) for item in value)


def validate_gate(value, pointer, errors, code="E_NEXT_ACTION_GATE"):
    if not isinstance(value, dict):
        add_error(errors, code, pointer, "completion gate must be an object")
        return
    if value.get("kind") not in GATE_KINDS or not nonempty_text(value.get("value")):
        add_error(
            errors,
            code,
            pointer,
            "completion gate requires an observable kind and non-empty value",
        )


def validate_action(value, pointer, errors, code="E_NEXT_ACTION_GATE"):
    if not isinstance(value, dict):
        add_error(errors, code, pointer, "action must be an object")
        return
    if not nonempty_text(value.get("action")) or not nonempty_text(value.get("owner")):
        add_error(errors, code, pointer, "action and owner must be non-empty")
    validate_gate(value.get("completion_gate"), f"{pointer}/completion_gate", errors, code)
    if "gap_ids" in value and not is_string_list(value.get("gap_ids")):
        add_error(errors, code, f"{pointer}/gap_ids", "gap_ids must be a string list")


def object_list(packet, field, errors):
    value = packet.get(field)
    if not isinstance(value, list):
        add_error(errors, "E_PACKET_SHAPE", f"/{field}", f"{field} must be a list")
        return []
    return value


def validate_packet(packet):
    errors = []
    if not isinstance(packet, dict):
        return [ValidationError("E_PACKET_SHAPE", "/", "packet must be an object")]

    for field in sorted(REQUIRED_FIELDS - set(packet)):
        add_error(errors, "E_PACKET_SHAPE", f"/{field}", "missing required field")
    if packet.get("schema_version") != "1.0":
        add_error(errors, "E_SCHEMA_VERSION", "/schema_version", "expected 1.0")
    mode = packet.get("mode")
    outcome = packet.get("outcome")
    if mode not in MODES:
        add_error(errors, "E_PACKET_SHAPE", "/mode", "invalid mode")
    if outcome not in OUTCOMES:
        add_error(errors, "E_PACKET_SHAPE", "/outcome", "invalid outcome")
    if not nonempty_text(packet.get("answer")):
        add_error(errors, "E_PACKET_SHAPE", "/answer", "answer must be non-empty")

    criteria = object_list(packet, "criteria", errors)
    options = object_list(packet, "options", errors)
    facts = object_list(packet, "supported_facts", errors)
    inferences = object_list(packet, "inferences", errors)
    assumptions = object_list(packet, "assumptions", errors)
    disputed = object_list(packet, "disputed_claims", errors)
    basis = object_list(packet, "decision_basis", errors)
    gaps = object_list(packet, "information_gaps", errors)

    criterion_ids = set()
    material_criteria = set()
    criterion_sources = []
    for index, criterion in enumerate(criteria):
        pointer = f"/criteria/{index}"
        if not isinstance(criterion, dict):
            add_error(errors, "E_PACKET_SHAPE", pointer, "criterion must be an object")
            continue
        identifier = criterion.get("id")
        if not valid_identifier(identifier):
            add_error(errors, "E_PACKET_SHAPE", f"{pointer}/id", "invalid criterion id")
        elif identifier in criterion_ids:
            add_error(errors, "E_DUPLICATE_ID", f"{pointer}/id", "duplicate criterion id")
        else:
            criterion_ids.add(identifier)
            if criterion.get("material") is True:
                material_criteria.add(identifier)
        if not nonempty_text(criterion.get("label")) or not isinstance(
            criterion.get("material"), bool
        ):
            add_error(errors, "E_PACKET_SHAPE", pointer, "invalid criterion fields")
        source_ids = criterion.get("source_ids")
        if not is_string_list(source_ids) or not source_ids:
            add_error(
                errors,
                "E_DANGLING_REFERENCE",
                f"{pointer}/source_ids",
                "criterion requires source ids",
            )
        else:
            criterion_sources.extend(
                (source, f"{pointer}/source_ids") for source in source_ids
            )

    claim_ids = {}
    claim_classes = {}
    normalized_classes = {}

    def register_claim(item, section, index):
        pointer = f"/{section}/{index}"
        if not isinstance(item, dict):
            add_error(errors, "E_PACKET_SHAPE", pointer, "claim entry must be an object")
            return None
        identifier = item.get("id")
        claim = item.get("claim")
        if not valid_identifier(identifier):
            add_error(errors, "E_PACKET_SHAPE", f"{pointer}/id", "invalid claim id")
            return None
        if identifier in claim_ids:
            add_error(errors, "E_DUPLICATE_ID", f"{pointer}/id", "duplicate claim id")
        else:
            claim_ids[identifier] = item
            claim_classes[identifier] = section
        if not nonempty_text(claim):
            add_error(errors, "E_PACKET_SHAPE", f"{pointer}/claim", "claim must be non-empty")
        else:
            normalized = normalized_claim(claim)
            prior = normalized_classes.get(normalized)
            if prior is not None and prior != section:
                add_error(
                    errors,
                    "E_EPISTEMIC_DUPLICATE",
                    f"{pointer}/claim",
                    f"claim duplicates epistemic class {prior}",
                )
            normalized_classes.setdefault(normalized, section)
        return identifier

    for index, fact in enumerate(facts):
        register_claim(fact, "supported_facts", index)
        if isinstance(fact, dict) and not safe_source(fact.get("source")):
            add_error(
                errors,
                "E_UNSAFE_SOURCE",
                f"/supported_facts/{index}/source",
                "unsafe source",
            )

    for index, inference in enumerate(inferences):
        register_claim(inference, "inferences", index)
        if isinstance(inference, dict) and (
            not is_string_list(inference.get("premise_ids"))
            or not inference.get("premise_ids")
        ):
            add_error(
                errors,
                "E_INFERENCE_PREMISE",
                f"/inferences/{index}/premise_ids",
                "premise_ids must be a string list",
            )

    for index, assumption in enumerate(assumptions):
        register_claim(assumption, "assumptions", index)
        pointer = f"/assumptions/{index}"
        if not isinstance(assumption, dict):
            continue
        if not nonempty_text(assumption.get("sensitivity")):
            add_error(
                errors,
                "E_PACKET_SHAPE",
                f"{pointer}/sensitivity",
                "sensitivity must be non-empty",
            )
        verification = assumption.get("verification")
        if not isinstance(verification, dict) or not nonempty_text(
            verification.get("action")
        ):
            add_error(
                errors,
                "E_PACKET_SHAPE",
                f"{pointer}/verification",
                "invalid verification",
            )
        else:
            validate_gate(
                verification.get("completion_gate"),
                f"{pointer}/verification/completion_gate",
                errors,
            )

    for index, item in enumerate(disputed):
        register_claim(item, "disputed_claims", index)
        pointer = f"/disputed_claims/{index}"
        if not isinstance(item, dict):
            continue
        if not safe_source(item.get("source")):
            add_error(errors, "E_UNSAFE_SOURCE", f"{pointer}/source", "unsafe source")
        if not nonempty_text(item.get("decision_use")):
            add_error(
                errors,
                "E_PACKET_SHAPE",
                f"{pointer}/decision_use",
                "decision_use must be non-empty",
            )

    critical_gap_ids = set()
    for index, gap in enumerate(gaps):
        identifier = register_claim(gap, "information_gaps", index)
        pointer = f"/information_gaps/{index}"
        if not isinstance(gap, dict):
            continue
        if not isinstance(gap.get("critical"), bool):
            add_error(
                errors,
                "E_PACKET_SHAPE",
                f"{pointer}/critical",
                "critical must be boolean",
            )
        elif gap.get("critical") and identifier:
            critical_gap_ids.add(identifier)
        verification = gap.get("verification")
        if not isinstance(verification, dict) or not nonempty_text(
            verification.get("action")
        ):
            add_error(
                errors,
                "E_PROCEDURAL_GAP",
                f"{pointer}/verification",
                "invalid gap verification",
            )
        else:
            validate_gate(
                verification.get("completion_gate"),
                f"{pointer}/verification/completion_gate",
                errors,
                "E_PROCEDURAL_GAP",
            )

    fact_ids = {
        item.get("id")
        for item in facts
        if isinstance(item, dict) and valid_identifier(item.get("id"))
    }
    inference_by_id = {
        item.get("id"): item
        for item in inferences
        if isinstance(item, dict) and valid_identifier(item.get("id"))
    }
    inference_ids = set(inference_by_id)
    eligible_ids = fact_ids | inference_ids

    for source_id, pointer in criterion_sources:
        if source_id not in fact_ids:
            add_error(
                errors,
                "E_DANGLING_REFERENCE",
                pointer,
                f"unknown supported fact: {source_id}",
            )

    for index, inference in enumerate(inferences):
        if not isinstance(inference, dict):
            continue
        for premise in inference.get("premise_ids", []):
            if premise not in claim_ids:
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    f"/inferences/{index}/premise_ids",
                    f"unknown premise: {premise}",
                )
            elif premise not in eligible_ids:
                add_error(
                    errors,
                    "E_INFERENCE_PREMISE",
                    f"/inferences/{index}/premise_ids",
                    f"ineligible premise: {premise}",
                )

    visiting = set()
    visited = set()

    def visit_inference(identifier):
        if identifier in visiting:
            add_error(
                errors,
                "E_INFERENCE_PREMISE",
                "/inferences",
                "cyclic inference premises",
            )
            return
        if identifier in visited or identifier not in inference_by_id:
            return
        visiting.add(identifier)
        for premise in inference_by_id[identifier].get("premise_ids", []):
            if premise in inference_by_id:
                visit_inference(premise)
        visiting.remove(identifier)
        visited.add(identifier)

    for inference_id in inference_ids:
        visit_inference(inference_id)

    option_ids = set()
    option_assessments = {}
    for option_index, option in enumerate(options):
        pointer = f"/options/{option_index}"
        if not isinstance(option, dict):
            add_error(errors, "E_PACKET_SHAPE", pointer, "option must be an object")
            continue
        identifier = option.get("id")
        if not valid_identifier(identifier):
            add_error(errors, "E_PACKET_SHAPE", f"{pointer}/id", "invalid option id")
            continue
        if identifier in option_ids:
            add_error(errors, "E_DUPLICATE_ID", f"{pointer}/id", "duplicate option id")
            continue
        option_ids.add(identifier)
        if not nonempty_text(option.get("label")):
            add_error(
                errors,
                "E_PACKET_SHAPE",
                f"{pointer}/label",
                "option label must be non-empty",
            )
        assessments = option.get("assessments")
        if not isinstance(assessments, list):
            add_error(
                errors,
                "E_CRITERION_COVERAGE",
                f"{pointer}/assessments",
                "assessments must be a list",
            )
            assessments = []
        by_criterion = {}
        for assessment_index, assessment in enumerate(assessments):
            assessment_pointer = f"{pointer}/assessments/{assessment_index}"
            if not isinstance(assessment, dict):
                add_error(
                    errors,
                    "E_PACKET_SHAPE",
                    assessment_pointer,
                    "assessment must be an object",
                )
                continue
            criterion_id = assessment.get("criterion_id")
            if criterion_id not in criterion_ids:
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    f"{assessment_pointer}/criterion_id",
                    "unknown criterion",
                )
                continue
            if criterion_id in by_criterion:
                add_error(
                    errors,
                    "E_CRITERION_COVERAGE",
                    f"{assessment_pointer}/criterion_id",
                    "duplicate assessment",
                )
            by_criterion[criterion_id] = assessment
            status = assessment.get("status")
            evidence_ids = assessment.get("evidence_ids")
            if status not in ASSESSMENTS or not is_string_list(evidence_ids):
                add_error(
                    errors,
                    "E_PACKET_SHAPE",
                    assessment_pointer,
                    "invalid assessment fields",
                )
                continue
            for evidence_id in evidence_ids:
                if evidence_id not in claim_ids:
                    add_error(
                        errors,
                        "E_DANGLING_REFERENCE",
                        f"{assessment_pointer}/evidence_ids",
                        f"unknown evidence: {evidence_id}",
                    )
                elif status in {"meets", "fails"} and evidence_id not in eligible_ids:
                    add_error(
                        errors,
                        "E_ASSESSMENT_EVIDENCE",
                        f"{assessment_pointer}/evidence_ids",
                        "assessment evidence is not eligible",
                    )
            if status in {"meets", "fails"} and not evidence_ids:
                add_error(
                    errors,
                    "E_ASSESSMENT_EVIDENCE",
                    f"{assessment_pointer}/evidence_ids",
                    "decisive assessment requires evidence",
                )
        missing = material_criteria - set(by_criterion)
        if missing:
            add_error(
                errors,
                "E_CRITERION_COVERAGE",
                f"{pointer}/assessments",
                f"missing material criteria: {', '.join(sorted(missing))}",
            )
        option_assessments[identifier] = by_criterion

    basis_ids = set()
    defeated_options = set()
    eligible_basis_count = 0
    for index, item in enumerate(basis):
        pointer = f"/decision_basis/{index}"
        if not isinstance(item, dict):
            add_error(errors, "E_SUBSTANTIVE_BASIS", pointer, "basis must be an object")
            continue
        identifier = item.get("id")
        if not valid_identifier(identifier) or identifier in basis_ids:
            add_error(
                errors,
                "E_DUPLICATE_ID",
                f"{pointer}/id",
                "invalid or duplicate basis id",
            )
        else:
            basis_ids.add(identifier)
        support_ids = item.get("support_ids")
        criterion_refs = item.get("criterion_ids")
        defeated_refs = item.get("defeats_option_ids")
        valid_basis = (
            nonempty_text(item.get("claim"))
            and is_string_list(support_ids)
            and bool(support_ids)
        )
        if not is_string_list(criterion_refs) or not criterion_refs:
            valid_basis = False
        if not isinstance(defeated_refs, list) or not all(
            valid_identifier(value) for value in defeated_refs
        ):
            valid_basis = False
            defeated_refs = []
        for support_id in support_ids if isinstance(support_ids, list) else []:
            if support_id not in claim_ids:
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    f"{pointer}/support_ids",
                    f"unknown support: {support_id}",
                )
                valid_basis = False
            elif support_id not in eligible_ids:
                valid_basis = False
        for criterion_id in (
            criterion_refs if isinstance(criterion_refs, list) else []
        ):
            if criterion_id not in material_criteria:
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    f"{pointer}/criterion_ids",
                    f"unknown material criterion: {criterion_id}",
                )
                valid_basis = False
        for option_id in defeated_refs:
            if option_id not in option_ids:
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    f"{pointer}/defeats_option_ids",
                    f"unknown option: {option_id}",
                )
                valid_basis = False
        if valid_basis:
            eligible_basis_count += 1
            defeated_options.update(defeated_refs)
        else:
            add_error(
                errors,
                "E_SUBSTANTIVE_BASIS",
                pointer,
                "basis requires eligible fact or inference support",
            )

    validate_action(packet.get("next_action"), "/next_action", errors)
    next_action = (
        packet.get("next_action") if isinstance(packet.get("next_action"), dict) else {}
    )
    gap_refs = next_action.get("gap_ids", [])
    effective_gap_refs = gap_refs
    if isinstance(gap_refs, list):
        for gap_id in gap_refs:
            if (
                gap_id not in claim_ids
                or claim_classes.get(gap_id) != "information_gaps"
            ):
                add_error(
                    errors,
                    "E_DANGLING_REFERENCE",
                    "/next_action/gap_ids",
                    f"unknown gap: {gap_id}",
                )

    for field, keys in (
        ("risks", ("risk", "safeguard")),
        ("change_conditions", ("condition", "effect")),
        ("material_dissent", ("claim", "consequence")),
    ):
        for index, item in enumerate(object_list(packet, field, errors)):
            if not isinstance(item, dict) or not all(
                nonempty_text(item.get(key)) for key in keys
            ):
                add_error(
                    errors,
                    "E_PACKET_SHAPE",
                    f"/{field}/{index}",
                    f"invalid {field} entry",
                )

    confidence = packet.get("confidence")
    if (
        not isinstance(confidence, dict)
        or confidence.get("evidence_quality") not in EVIDENCE_QUALITIES
        or confidence.get("independence") not in INDEPENDENCE_LEVELS
        or not nonempty_text(confidence.get("evidence_reason"))
        or not nonempty_text(confidence.get("independence_note"))
        or not is_string_list(confidence.get("residual_uncertainty"))
    ):
        add_error(
            errors,
            "E_CONFIDENCE",
            "/confidence",
            "invalid separated confidence fields",
        )

    coverage = packet.get("coverage")
    coverage_fields = (
        "consulted_sources",
        "omitted_sources",
        "limitations",
        "failures",
    )
    if not isinstance(coverage, dict) or not all(
        is_string_list(coverage.get(field)) for field in coverage_fields
    ):
        add_error(
            errors,
            "E_PACKET_SHAPE",
            "/coverage",
            "invalid coverage fields",
        )
    elif any(
        not safe_source(source)
        for source in coverage["consulted_sources"] + coverage["omitted_sources"]
    ):
        add_error(errors, "E_UNSAFE_SOURCE", "/coverage", "unsafe coverage source")

    if mode == "review":
        review = packet.get("review")
        if not isinstance(review, dict):
            add_error(
                errors,
                "E_MODE_CONTENT",
                "/review",
                "review content is required",
            )
        else:
            findings = review.get("prioritized_findings")
            if not isinstance(findings, list) or not findings:
                add_error(
                    errors,
                    "E_MODE_CONTENT",
                    "/review/prioritized_findings",
                    "findings are required",
                )
            else:
                for index, finding in enumerate(findings):
                    if (
                        not isinstance(finding, dict)
                        or finding.get("severity")
                        not in {"critical", "important", "minor"}
                        or not nonempty_text(finding.get("finding"))
                        or not is_string_list(finding.get("evidence_ids"))
                        or not finding.get("evidence_ids")
                    ):
                        add_error(
                            errors,
                            "E_MODE_CONTENT",
                            f"/review/prioritized_findings/{index}",
                            "invalid finding",
                        )
                    elif any(
                        evidence_id not in claim_ids
                        for evidence_id in finding["evidence_ids"]
                    ):
                        add_error(
                            errors,
                            "E_DANGLING_REFERENCE",
                            f"/review/prioritized_findings/{index}/evidence_ids",
                            "unknown finding evidence",
                        )
                    elif any(
                        evidence_id not in eligible_ids
                        for evidence_id in finding["evidence_ids"]
                    ):
                        add_error(
                            errors,
                            "E_MODE_CONTENT",
                            f"/review/prioritized_findings/{index}/evidence_ids",
                            "finding evidence is not eligible",
                        )
            if not is_string_list(
                review.get("recommended_changes")
            ) or not is_string_list(review.get("strengths_to_preserve")):
                add_error(
                    errors,
                    "E_MODE_CONTENT",
                    "/review",
                    "review lists are required",
                )
            validate_action(
                review.get("next_validation_step"),
                "/review/next_validation_step",
                errors,
                "E_MODE_CONTENT",
            )
            if isinstance(review.get("next_validation_step"), dict):
                effective_gap_refs = review["next_validation_step"].get(
                    "gap_ids", []
                )
                if isinstance(effective_gap_refs, list):
                    for gap_id in effective_gap_refs:
                        if (
                            gap_id not in claim_ids
                            or claim_classes.get(gap_id) != "information_gaps"
                        ):
                            add_error(
                                errors,
                                "E_DANGLING_REFERENCE",
                                "/review/next_validation_step/gap_ids",
                                f"unknown gap: {gap_id}",
                            )
    if mode == "synthesize":
        synthesis = packet.get("synthesis")
        if not isinstance(synthesis, dict):
            add_error(
                errors,
                "E_MODE_CONTENT",
                "/synthesis",
                "synthesis content is required",
            )
        else:
            if not is_string_list(
                synthesis.get("implications")
            ) or not is_string_list(synthesis.get("imported_analyses")) or not synthesis.get(
                "imported_analyses"
            ):
                add_error(
                    errors,
                    "E_MODE_CONTENT",
                    "/synthesis",
                    "synthesis lists are required",
                )
            differences = synthesis.get("irreducible_differences")
            if not isinstance(differences, list):
                add_error(
                    errors,
                    "E_MODE_CONTENT",
                    "/synthesis/irreducible_differences",
                    "differences must be a list",
                )
            elif any(
                not isinstance(item, dict)
                or not nonempty_text(item.get("difference"))
                or not is_string_list(item.get("assumption_ids"))
                for item in differences
            ):
                add_error(
                    errors,
                    "E_MODE_CONTENT",
                    "/synthesis/irreducible_differences",
                    "invalid difference",
                )
            else:
                for index, item in enumerate(differences):
                    for assumption_id in item["assumption_ids"]:
                        if (
                            assumption_id not in claim_ids
                            or claim_classes.get(assumption_id) != "assumptions"
                        ):
                            add_error(
                                errors,
                                "E_DANGLING_REFERENCE",
                                f"/synthesis/irreducible_differences/{index}/assumption_ids",
                                f"unknown assumption: {assumption_id}",
                            )
            if isinstance(synthesis.get("imported_analyses"), list) and any(
                not safe_source(source)
                for source in synthesis["imported_analyses"]
            ):
                add_error(
                    errors,
                    "E_UNSAFE_SOURCE",
                    "/synthesis/imported_analyses",
                    "unsafe imported analysis source",
                )

    selected = packet.get("selected_option_id")
    if outcome == "substantive":
        if not material_criteria:
            add_error(
                errors,
                "E_CRITERION_COVERAGE",
                "/criteria",
                "substantive outcome requires a material criterion",
            )
        if selected not in option_ids:
            add_error(
                errors,
                "E_SELECTED_CRITERION",
                "/selected_option_id",
                "substantive outcome requires an existing selected option",
            )
        else:
            for criterion_id in material_criteria:
                assessment = option_assessments.get(selected, {}).get(criterion_id)
                if (
                    not assessment
                    or assessment.get("status") != "meets"
                    or not assessment.get("evidence_ids")
                    or any(
                        evidence not in eligible_ids
                        for evidence in assessment.get("evidence_ids", [])
                    )
                ):
                    add_error(
                        errors,
                        "E_SELECTED_CRITERION",
                        f"/options/{selected}/assessments/{criterion_id}",
                        "selected option must meet every material criterion with eligible evidence",
                    )
        if eligible_basis_count == 0:
            add_error(
                errors,
                "E_SUBSTANTIVE_BASIS",
                "/decision_basis",
                "substantive outcome requires eligible basis",
            )
        alternatives = option_ids - ({selected} if selected in option_ids else set())
        undefeated = alternatives - defeated_options
        if undefeated:
            add_error(
                errors,
                "E_ALTERNATIVE_NOT_DEFEATED",
                "/decision_basis",
                f"material alternatives not defeated: {', '.join(sorted(undefeated))}",
            )
    elif outcome == "procedural":
        if selected is not None:
            add_error(
                errors,
                "E_PROCEDURAL_SELECTION",
                "/selected_option_id",
                "procedural outcome cannot select an option",
            )
        if basis:
            add_error(
                errors,
                "E_PROCEDURAL_SELECTION",
                "/decision_basis",
                "procedural outcome cannot retain decision basis",
            )
        if not critical_gap_ids or not critical_gap_ids.intersection(
            effective_gap_refs if isinstance(effective_gap_refs, list) else []
        ):
            add_error(
                errors,
                "E_PROCEDURAL_GAP",
                "/information_gaps",
                "procedural outcome requires a critical gap closed by next_action",
            )

    return sorted(
        set(errors), key=lambda error: (error.pointer, error.code, error.message)
    )


def load_packet(path):
    try:
        if path.stat().st_size > MAX_PACKET_BYTES:
            return None, [
                ValidationError("E_PACKET_READ", "/", "packet exceeds 1 MiB")
            ]
        packet = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, [ValidationError("E_PACKET_READ", "/", str(error))]
    return packet, []


def format_errors(errors):
    return "\n".join(
        f"{error.code} {error.pointer} {error.message}" for error in errors
    )


def main(argv):
    if len(argv) != 1:
        print("usage: check_decision_packet.py PACKET", file=sys.stderr)
        return 2
    packet, read_errors = load_packet(Path(argv[0]))
    if read_errors:
        print(format_errors(read_errors), file=sys.stderr)
        return 2
    errors = validate_packet(packet)
    if errors:
        print(format_errors(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
