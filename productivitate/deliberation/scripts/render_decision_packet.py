"""Render only validated deliberation decision packets."""

import argparse
import importlib.util
import sys
import unicodedata
from pathlib import Path


HEADINGS = {
    "decide": (
        "## Recommendation", "## Why", "## Next action",
        "## Risks and safeguards", "## What would change the recommendation",
        "## Confidence", "## Material dissent", "## Coverage and limitations",
    ),
    "review": (
        "## Verdict", "## Prioritized findings", "## Recommended changes",
        "## Next validation step", "## Strengths to preserve",
        "## Risks and safeguards", "## What would change the verdict",
        "## Confidence", "## Material dissent", "## Coverage and limitations",
    ),
    "synthesize": (
        "## Combined conclusion", "## Why", "## Implications and next action",
        "## Irreducible differences", "## What would change the conclusion",
        "## Confidence", "## Material dissent", "## Coverage and limitations",
    ),
}


def load_validator():
    path = Path(__file__).resolve().with_name("check_decision_packet.py")
    spec = importlib.util.spec_from_file_location(
        "deliberation_decision_packet_validator", path
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load packet validator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_validator()


def clean_text(value):
    text = unicodedata.normalize("NFKC", str(value))
    text = "".join(
        character if character >= " " and character != "\x7f" else " "
        for character in text
    )
    text = " ".join(text.split())
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace(chr(96), "'")
        .replace("#", r"\#")
    )


def bullet_lines(values, empty="None."):
    cleaned = [clean_text(value) for value in values if clean_text(value)]
    return "\n".join(f"- {value}" for value in cleaned) if cleaned else empty


def render_action(action):
    gate = action["completion_gate"]
    return "\n\n".join(
        (
            f"**Owner:** {clean_text(action['owner'])}",
            f"**Action:** {clean_text(action['action'])}",
            f"**Completion gate ({clean_text(gate['kind'])}):** "
            f"{clean_text(gate['value'])}",
        )
    )


def render_reasoning(packet):
    lines = []
    for item in packet["decision_basis"]:
        lines.append(f"- **Decision basis:** {clean_text(item['claim'])}")
    for item in packet["supported_facts"]:
        lines.append(
            f"- **Supported fact:** {clean_text(item['claim'])} "
            f"(Source: {clean_text(item['source'])})"
        )
    for item in packet["inferences"]:
        premises = ", ".join(clean_text(value) for value in item["premise_ids"])
        lines.append(
            f"- **Inference:** {clean_text(item['claim'])} (Premises: {premises})"
        )
    for item in packet["assumptions"]:
        verification = item["verification"]
        gate = verification["completion_gate"]
        lines.append(
            f"- **Assumption:** {clean_text(item['claim'])} "
            f"(Sensitivity: {clean_text(item['sensitivity'])}; "
            f"Requires verification: {clean_text(verification['action'])}; "
            f"{clean_text(gate['kind'])}: {clean_text(gate['value'])})"
        )
    for item in packet["disputed_claims"]:
        lines.append(
            f"- **Disputed or untrusted claim:** {clean_text(item['claim'])} "
            f"(Source: {clean_text(item['source'])}; "
            f"Decision use: {clean_text(item['decision_use'])})"
        )
    for item in packet["information_gaps"]:
        verification = item["verification"]
        gate = verification["completion_gate"]
        lines.append(
            f"- **Requires verification:** {clean_text(item['claim'])} "
            f"(Check: {clean_text(verification['action'])}; "
            f"{clean_text(gate['kind'])}: {clean_text(gate['value'])})"
        )
    return "\n".join(lines) if lines else "No additional reasoning entries."


def render_risks(packet):
    return bullet_lines(
        f"{item['risk']} — Safeguard: {item['safeguard']}"
        for item in packet["risks"]
    )


def render_changes(packet):
    return bullet_lines(
        f"{item['condition']} — Effect: {item['effect']}"
        for item in packet["change_conditions"]
    )


def render_confidence(packet):
    confidence = packet["confidence"]
    residual = "; ".join(
        clean_text(value) for value in confidence["residual_uncertainty"]
    ) or "None recorded."
    return "\n".join(
        (
            f"- **Evidence quality:** {clean_text(confidence['evidence_quality'])} — "
            f"{clean_text(confidence['evidence_reason'])}",
            f"- **Independence:** {clean_text(confidence['independence'])} — "
            f"{clean_text(confidence['independence_note'])}",
            f"- **Residual uncertainty:** {residual}",
        )
    )


def render_dissent(packet):
    return bullet_lines(
        f"{item['claim']} — Consequence: {item['consequence']}"
        for item in packet["material_dissent"]
    )


def render_coverage(packet):
    coverage = packet["coverage"]

    def joined(field):
        return ", ".join(clean_text(value) for value in coverage[field]) or "none"

    return "\n".join(
        (
            f"- **Consulted sources:** {joined('consulted_sources')}",
            f"- **Omitted sources:** {joined('omitted_sources')}",
            f"- **Limitations:** {joined('limitations')}",
            f"- **Failures or downgrades:** {joined('failures')}",
        )
    )


def render_decide(packet):
    return (
        clean_text(packet["answer"]),
        render_reasoning(packet),
        render_action(packet["next_action"]),
        render_risks(packet),
        render_changes(packet),
        render_confidence(packet),
        render_dissent(packet),
        render_coverage(packet),
    )


def render_review(packet):
    review = packet["review"]
    findings = bullet_lines(
        f"[{item['severity'].upper()}] {item['finding']} "
        f"(Evidence: {', '.join(item['evidence_ids'])})"
        for item in review["prioritized_findings"]
    )
    return (
        clean_text(packet["answer"]),
        findings,
        bullet_lines(review["recommended_changes"]),
        render_action(review["next_validation_step"]),
        bullet_lines(review["strengths_to_preserve"]),
        render_risks(packet),
        render_changes(packet),
        render_confidence(packet),
        render_dissent(packet),
        render_coverage(packet),
    )


def render_synthesize(packet):
    synthesis = packet["synthesis"]
    implications = bullet_lines(synthesis["implications"])
    action = render_action(packet["next_action"])
    differences = bullet_lines(
        f"{item['difference']} "
        f"(Assumptions: {', '.join(item['assumption_ids']) or 'none'})"
        for item in synthesis["irreducible_differences"]
    )
    return (
        clean_text(packet["answer"]),
        render_reasoning(packet),
        f"{implications}\n\n{action}",
        differences,
        render_changes(packet),
        render_confidence(packet),
        render_dissent(packet),
        render_coverage(packet),
    )


def assemble(mode, sections):
    return "\n\n".join(
        f"{heading}\n{body}" for heading, body in zip(HEADINGS[mode], sections)
    ) + "\n"


def render_packet(packet):
    errors = VALIDATOR.validate_packet(packet)
    if errors:
        raise ValueError(VALIDATOR.format_errors(errors))
    if packet["mode"] == "review":
        sections = render_review(packet)
    elif packet["mode"] == "synthesize":
        sections = render_synthesize(packet)
    else:
        sections = render_decide(packet)
    return assemble(packet["mode"], sections)


def safe_sections(mode, error_codes):
    codes = bullet_lines(error_codes)
    confidence = "\n".join(
        (
            "- **Evidence quality:** insufficient — the decision packet failed deterministic validation.",
            "- **Independence:** L0 — finalization failure does not establish independent consensus.",
            "- **Residual uncertainty:** the invalid packet must not support a substantive conclusion.",
        )
    )
    coverage = (
        "- **Consulted sources:** none added during repair\n"
        "- **Omitted sources:** unknown\n"
        "- **Limitations:** guarded finalization failed\n"
        "- **Failures or downgrades:** one packet repair was exhausted"
    )
    action = (
        "**Owner:** human reviewer\n\n"
        "**Action:** Inspect the packet validation errors.\n\n"
        "**Completion gate (state):** Every reported code is resolved and the packet validates."
    )
    if mode == "review":
        return (
            "Defer the verdict. Guarded finalization failed and requires human review.",
            f"- **CRITICAL:** Packet validation failed.\n{codes}",
            "- Correct only the reported packet fields; do not ship the reviewed artifact.",
            action,
            "Preserve only source-backed content from the invalid packet.",
            "- Risk: publishing an invalid verdict. — Safeguard: keep the artifact unchanged.",
            "- A packet that passes deterministic validation would reopen the verdict.",
            confidence,
            "No validated dissent can be reported from the failed packet.",
            coverage,
        )
    if mode == "synthesize":
        return (
            "The supplied packet does not support a substantive combined conclusion.",
            f"Guarded finalization reported:\n{codes}",
            action,
            "The invalid packet cannot establish which differences are irreducible.",
            "- A packet that passes deterministic validation would reopen synthesis.",
            confidence,
            "No validated dissent can be reported from the failed packet.",
            coverage,
        )
    return (
        "Do not decide yet. Guarded finalization failed and requires human review.",
        f"Guarded finalization reported:\n{codes}",
        action,
        "- Risk: publishing an invalid recommendation. — Safeguard: keep the current state unchanged.",
        "- A packet that passes deterministic validation would reopen the recommendation.",
        confidence,
        "No validated dissent can be reported from the failed packet.",
        coverage,
    )


def render_safe_failure(mode, errors):
    safe_mode = mode if mode in HEADINGS else "decide"
    error_codes = sorted({clean_text(error.code) for error in errors})
    return assemble(safe_mode, safe_sections(safe_mode, error_codes))


def write_output(markdown, output):
    if output is None:
        sys.stdout.write(markdown)
        return None
    try:
        output.write_text(markdown, encoding="utf-8")
    except OSError as error:
        return str(error)
    return None


def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="render_decision_packet.py",
        description="Render a validated deliberation decision packet.",
    )
    parser.add_argument("--safe-failure", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("packet", type=Path)
    return parser.parse_args(argv)


def main(argv):
    arguments = parse_args(argv)
    packet, read_errors = VALIDATOR.load_packet(arguments.packet)
    if read_errors:
        if arguments.safe_failure:
            markdown = render_safe_failure("decide", read_errors)
            write_error = write_output(markdown, arguments.output)
            if write_error:
                print(write_error, file=sys.stderr)
                return 2
            print(VALIDATOR.format_errors(read_errors), file=sys.stderr)
            return 3
        print(VALIDATOR.format_errors(read_errors), file=sys.stderr)
        return 2

    errors = VALIDATOR.validate_packet(packet)
    if errors:
        if arguments.safe_failure:
            mode = packet.get("mode") if isinstance(packet, dict) else "decide"
            markdown = render_safe_failure(mode, errors)
            write_error = write_output(markdown, arguments.output)
            if write_error:
                print(write_error, file=sys.stderr)
                return 2
            print(VALIDATOR.format_errors(errors), file=sys.stderr)
            return 3
        print(VALIDATOR.format_errors(errors), file=sys.stderr)
        return 1

    markdown = render_packet(packet)
    write_error = write_output(markdown, arguments.output)
    if write_error:
        print(write_error, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
