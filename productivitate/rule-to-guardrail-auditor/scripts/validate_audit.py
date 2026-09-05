#!/usr/bin/env python3
"""Validate a Rule-to-Guardrail Auditor V1 JSON packet without mutating it."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


TOP_LEVEL_KEYS = {
    "schema_version",
    "audit_id",
    "created_at",
    "mode",
    "target_platforms",
    "sources",
    "instructions",
    "contradictions",
    "ambiguities",
    "coverage",
    "attestation",
}
SOURCE_KEYS = {"id", "kind", "locator", "status", "note"}
INSTRUCTION_KEYS = {
    "id",
    "source_id",
    "location",
    "original",
    "normalized",
    "disposition",
    "confidence",
    "rationale",
    "details",
    "platform_feasibility",
}
PLATFORM_RECORD_KEYS = {"platform", "feasibility", "mechanism", "evidence"}
CONTRADICTION_KEYS = {
    "id",
    "instruction_ids",
    "overlapping_condition",
    "incompatible_outcomes",
    "resolution_question",
}
AMBIGUITY_KEYS = {
    "id",
    "instruction_id",
    "unclear_term",
    "impact",
    "resolving_question",
}
COVERAGE_KEYS = {
    "sources_total",
    "sources_processed",
    "sources_skipped",
    "sources_unreadable",
    "sources_incomplete",
    "instructions_total",
    "dispositions",
}
ATTESTATION_KEYS = {
    "modified_sources",
    "installed_controls",
    "executed_tests",
    "accessed_secrets",
    "published",
    "deployed",
    "sent_messages",
    "statement",
}
DISPOSITIONS = {"RULE", "CONTROL", "ELIMINATE", "HUMAN_DECISION"}
PLATFORMS = {"generic", "codex", "claude"}
FEASIBILITY = {"native", "scripted", "advisory_only", "unverified"}
CONFIDENCE = {"low", "medium", "high"}
SOURCE_KINDS = {"file", "pasted"}
SOURCE_STATUSES = {"processed", "skipped", "unreadable", "incomplete"}
ELIMINATE_REASONS = {"vague", "duplicate", "obsolete", "contradicted", "non_actionable"}
NON_MUTATION_STATEMENT = (
    "No audited source, control, hook, configuration, or permission was modified."
)
DETAIL_KEYS = {
    "RULE": {
        "retained_instruction",
        "judgment_required",
        "anti_pattern",
        "review_question",
    },
    "CONTROL": {
        "trigger",
        "condition",
        "enforcement_point",
        "allow_behavior",
        "failure_behavior",
        "positive_test",
        "negative_test",
        "limitations",
        "control_status",
    },
    "ELIMINATE": {"reason", "replacement", "related_instruction_ids"},
    "HUMAN_DECISION": {
        "decision_owner",
        "approval_moment",
        "information_required",
        "prohibited_before_approval",
        "retained_risk",
    },
}


def _closed_keys(value: Any, required: set[str], path: str, errors: list[str]) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{path}: expected object")
        return False
    for key in sorted(required - set(value)):
        errors.append(f"{path}: missing required key '{key}'")
    for key in sorted(set(value) - required):
        errors.append(f"{path}: unknown key '{key}'")
    return True


def _nonempty_string(value: Any, path: str, errors: list[str]) -> bool:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path}: expected non-empty string")
        return False
    return True


def _enum(value: Any, allowed: set[str], path: str, errors: list[str]) -> bool:
    if value not in allowed:
        errors.append(f"{path}: invalid value {value!r}")
        return False
    return True


def _list(value: Any, path: str, errors: list[str]) -> bool:
    if not isinstance(value, list):
        errors.append(f"{path}: expected array")
        return False
    return True


def _validate_platform_records(
    value: Any, target_platforms: set[str], path: str, errors: list[str]
) -> None:
    if not _list(value, path, errors):
        return
    observed: list[str] = []
    for index, record in enumerate(value):
        record_path = f"{path}[{index}]"
        if not _closed_keys(record, PLATFORM_RECORD_KEYS, record_path, errors):
            continue
        platform = record.get("platform")
        if _nonempty_string(platform, f"{record_path}.platform", errors):
            _enum(platform, PLATFORMS, f"{record_path}.platform", errors)
            if platform in observed:
                errors.append(f"{record_path}.platform: duplicate value {platform!r}")
            observed.append(platform)
        _enum(record.get("feasibility"), FEASIBILITY, f"{record_path}.feasibility", errors)
        _nonempty_string(record.get("mechanism"), f"{record_path}.mechanism", errors)
        _nonempty_string(record.get("evidence"), f"{record_path}.evidence", errors)
    if set(observed) != target_platforms or len(observed) != len(target_platforms):
        errors.append(
            f"{path}: expected platforms {sorted(target_platforms)!r}, got {sorted(observed)!r}"
        )


def validate_instruction(
    record: object, source_ids: set[str], target_platforms: set[str], index: int
) -> list[str]:
    errors: list[str] = []
    path = f"$.instructions[{index}]"
    if not _closed_keys(record, INSTRUCTION_KEYS, path, errors):
        return errors
    assert isinstance(record, dict)

    for key in ("id", "source_id", "location", "original", "normalized", "rationale"):
        _nonempty_string(record.get(key), f"{path}.{key}", errors)
    source_id = record.get("source_id")
    if isinstance(source_id, str) and source_id not in source_ids:
        errors.append(f"{path}.source_id: unknown source id {source_id!r}")

    disposition = record.get("disposition")
    disposition_valid = _enum(disposition, DISPOSITIONS, f"{path}.disposition", errors)
    _enum(record.get("confidence"), CONFIDENCE, f"{path}.confidence", errors)

    details = record.get("details")
    if disposition_valid:
        required = DETAIL_KEYS[disposition]
        if _closed_keys(details, required, f"{path}.details", errors):
            assert isinstance(details, dict)
            for key in required:
                if key == "related_instruction_ids":
                    if _list(details.get(key), f"{path}.details.{key}", errors):
                        for related_index, related_id in enumerate(details[key]):
                            _nonempty_string(
                                related_id,
                                f"{path}.details.{key}[{related_index}]",
                                errors,
                            )
                else:
                    _nonempty_string(details.get(key), f"{path}.details.{key}", errors)
            if disposition == "CONTROL" and details.get("control_status") != "proposed":
                errors.append(
                    f"{path}.details.control_status: expected 'proposed', got {details.get('control_status')!r}"
                )
            if disposition == "ELIMINATE":
                reason = details.get("reason")
                _enum(reason, ELIMINATE_REASONS, f"{path}.details.reason", errors)
                if reason in {"duplicate", "contradicted"} and not details.get(
                    "related_instruction_ids"
                ):
                    errors.append(
                        f"{path}.details.related_instruction_ids: expected at least one id "
                        f"for reason {reason!r}"
                    )
    else:
        if not isinstance(details, dict):
            errors.append(f"{path}.details: expected object")

    _validate_platform_records(
        record.get("platform_feasibility"), target_platforms, f"{path}.platform_feasibility", errors
    )
    return errors


def _validate_created_at(value: Any, errors: list[str]) -> None:
    if not _nonempty_string(value, "$.created_at", errors):
        return
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append("$.created_at: expected ISO-8601 timestamp")
        return
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        errors.append("$.created_at: must include a timezone")


def _validate_sources(value: Any, errors: list[str]) -> tuple[set[str], Counter[str]]:
    source_ids: set[str] = set()
    statuses: Counter[str] = Counter()
    if not _list(value, "$.sources", errors):
        return source_ids, statuses
    for index, source in enumerate(value):
        path = f"$.sources[{index}]"
        if not _closed_keys(source, SOURCE_KEYS, path, errors):
            continue
        assert isinstance(source, dict)
        for key in ("id", "locator", "note"):
            _nonempty_string(source.get(key), f"{path}.{key}", errors)
        source_id = source.get("id")
        if isinstance(source_id, str):
            if source_id in source_ids:
                errors.append(f"{path}.id: duplicate id {source_id!r}")
            source_ids.add(source_id)
        _enum(source.get("kind"), SOURCE_KINDS, f"{path}.kind", errors)
        status = source.get("status")
        if _enum(status, SOURCE_STATUSES, f"{path}.status", errors):
            statuses[status] += 1
    return source_ids, statuses


def _validate_instruction_list(
    value: Any, source_ids: set[str], target_platforms: set[str], errors: list[str]
) -> tuple[set[str], Counter[str]]:
    instruction_ids: set[str] = set()
    dispositions: Counter[str] = Counter()
    if not _list(value, "$.instructions", errors):
        return instruction_ids, dispositions
    for index, record in enumerate(value):
        errors.extend(validate_instruction(record, source_ids, target_platforms, index))
        if not isinstance(record, dict):
            continue
        instruction_id = record.get("id")
        if isinstance(instruction_id, str):
            if instruction_id in instruction_ids:
                errors.append(f"$.instructions[{index}].id: duplicate id {instruction_id!r}")
            instruction_ids.add(instruction_id)
        disposition = record.get("disposition")
        if disposition in DISPOSITIONS:
            dispositions[disposition] += 1

    for index, record in enumerate(value):
        if not isinstance(record, dict) or record.get("disposition") != "ELIMINATE":
            continue
        details = record.get("details")
        if not isinstance(details, dict):
            continue
        for related_index, related_id in enumerate(details.get("related_instruction_ids", [])):
            if related_id not in instruction_ids:
                errors.append(
                    f"$.instructions[{index}].details.related_instruction_ids[{related_index}]: "
                    f"unknown instruction id {related_id!r}"
                )
    return instruction_ids, dispositions


def _validate_contradictions(value: Any, instruction_ids: set[str], errors: list[str]) -> None:
    if not _list(value, "$.contradictions", errors):
        return
    observed_ids: set[str] = set()
    for index, record in enumerate(value):
        path = f"$.contradictions[{index}]"
        if not _closed_keys(record, CONTRADICTION_KEYS, path, errors):
            continue
        assert isinstance(record, dict)
        for key in ("id", "overlapping_condition", "incompatible_outcomes", "resolution_question"):
            _nonempty_string(record.get(key), f"{path}.{key}", errors)
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in observed_ids:
                errors.append(f"{path}.id: duplicate id {record_id!r}")
            observed_ids.add(record_id)
        refs = record.get("instruction_ids")
        if not _list(refs, f"{path}.instruction_ids", errors):
            continue
        if len(refs) != 2:
            errors.append(f"{path}.instruction_ids: expected exactly 2 values")
        if len(refs) == 2 and refs[0] == refs[1]:
            errors.append(f"{path}.instruction_ids: values must be distinct")
        for ref_index, instruction_id in enumerate(refs):
            if instruction_id not in instruction_ids:
                errors.append(
                    f"{path}.instruction_ids[{ref_index}]: unknown instruction id {instruction_id!r}"
                )


def _validate_ambiguities(value: Any, instruction_ids: set[str], errors: list[str]) -> None:
    if not _list(value, "$.ambiguities", errors):
        return
    observed_ids: set[str] = set()
    for index, record in enumerate(value):
        path = f"$.ambiguities[{index}]"
        if not _closed_keys(record, AMBIGUITY_KEYS, path, errors):
            continue
        assert isinstance(record, dict)
        for key in ("id", "instruction_id", "unclear_term", "impact", "resolving_question"):
            _nonempty_string(record.get(key), f"{path}.{key}", errors)
        record_id = record.get("id")
        if isinstance(record_id, str):
            if record_id in observed_ids:
                errors.append(f"{path}.id: duplicate id {record_id!r}")
            observed_ids.add(record_id)
        instruction_id = record.get("instruction_id")
        if isinstance(instruction_id, str) and instruction_id not in instruction_ids:
            errors.append(f"{path}.instruction_id: unknown instruction id {instruction_id!r}")


def _validate_coverage(
    value: Any,
    source_count: int,
    statuses: Counter[str],
    instruction_count: int,
    dispositions: Counter[str],
    errors: list[str],
) -> None:
    if not _closed_keys(value, COVERAGE_KEYS, "$.coverage", errors):
        return
    assert isinstance(value, dict)
    expected_counts = {
        "sources_total": source_count,
        "sources_processed": statuses["processed"],
        "sources_skipped": statuses["skipped"],
        "sources_unreadable": statuses["unreadable"],
        "sources_incomplete": statuses["incomplete"],
        "instructions_total": instruction_count,
    }
    for key, expected in expected_counts.items():
        actual = value.get(key)
        if type(actual) is not int or actual < 0:
            errors.append(f"$.coverage.{key}: expected non-negative integer")
        elif actual != expected:
            errors.append(f"$.coverage.{key}: expected {expected}, got {actual}")

    disposition_counts = value.get("dispositions")
    if not _closed_keys(disposition_counts, DISPOSITIONS, "$.coverage.dispositions", errors):
        return
    assert isinstance(disposition_counts, dict)
    for disposition in sorted(DISPOSITIONS):
        actual = disposition_counts.get(disposition)
        expected = dispositions[disposition]
        if type(actual) is not int or actual < 0:
            errors.append(
                f"$.coverage.dispositions.{disposition}: expected non-negative integer"
            )
        elif actual != expected:
            errors.append(
                f"$.coverage.dispositions.{disposition}: expected {expected}, got {actual}"
            )


def _validate_attestation(value: Any, errors: list[str]) -> None:
    if not _closed_keys(value, ATTESTATION_KEYS, "$.attestation", errors):
        return
    assert isinstance(value, dict)
    for key in ATTESTATION_KEYS - {"statement"}:
        if value.get(key) is not False:
            errors.append(f"$.attestation.{key}: must be false")
    if value.get("statement") != NON_MUTATION_STATEMENT:
        errors.append(f"$.attestation.statement: expected {NON_MUTATION_STATEMENT!r}")


def validate_packet(packet: object) -> list[str]:
    """Return deterministic contract errors; an empty list means valid."""
    errors: list[str] = []
    if not _closed_keys(packet, TOP_LEVEL_KEYS, "$", errors):
        return errors
    assert isinstance(packet, dict)

    if packet.get("schema_version") != "1.0":
        errors.append("$.schema_version: expected '1.0'")
    audit_id = packet.get("audit_id")
    if not _nonempty_string(audit_id, "$.audit_id", errors) or not re.fullmatch(
        r"r2g-\d{8}-[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", str(audit_id)
    ):
        errors.append("$.audit_id: expected r2g-YYYYMMDD-lowercase-slug")
    _validate_created_at(packet.get("created_at"), errors)
    if packet.get("mode") != "consultative":
        errors.append("$.mode: expected 'consultative'")

    target_platforms: set[str] = set()
    platforms_value = packet.get("target_platforms")
    if _list(platforms_value, "$.target_platforms", errors):
        if not platforms_value:
            errors.append("$.target_platforms: expected at least one platform")
        observed_platforms: list[str] = []
        for index, platform in enumerate(platforms_value):
            if _enum(platform, PLATFORMS, f"$.target_platforms[{index}]", errors):
                if platform in observed_platforms:
                    errors.append(f"$.target_platforms[{index}]: duplicate value {platform!r}")
                observed_platforms.append(platform)
                target_platforms.add(platform)

    sources_value = packet.get("sources")
    source_ids, statuses = _validate_sources(sources_value, errors)
    instructions_value = packet.get("instructions")
    instruction_ids, dispositions = _validate_instruction_list(
        instructions_value, source_ids, target_platforms, errors
    )
    _validate_contradictions(packet.get("contradictions"), instruction_ids, errors)
    _validate_ambiguities(packet.get("ambiguities"), instruction_ids, errors)
    _validate_coverage(
        packet.get("coverage"),
        len(sources_value) if isinstance(sources_value, list) else 0,
        statuses,
        len(instructions_value) if isinstance(instructions_value, list) else 0,
        dispositions,
        errors,
    )
    _validate_attestation(packet.get("attestation"), errors)
    return errors


def load_packet(path: Path) -> object:
    """Read and parse one JSON audit packet."""
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: validate_audit.py <audit.json>", file=sys.stderr)
        return 2
    path = Path(args[0])
    try:
        packet = load_packet(path)
    except OSError as error:
        print(f"cannot read {path}: {error}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as error:
        print(f"invalid JSON in {path}: {error.msg}", file=sys.stderr)
        return 2

    errors = validate_packet(packet)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    assert isinstance(packet, dict)
    print(f"VALID {packet['audit_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
