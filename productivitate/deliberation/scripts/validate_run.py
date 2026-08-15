"""Validate a persisted deliberation dossier without runtime dependencies."""

import json
import sys
from pathlib import Path, PureWindowsPath


REQUIRED_FIELDS = (
    "schema_version",
    "run_id",
    "mode",
    "depth",
    "status",
    "independence_level",
    "brief",
    "context_manifest",
    "perspectives",
    "challenge",
    "fusion",
    "final",
    "failures",
)
PERSPECTIVE_FIELDS = (
    "id",
    "executor",
    "model_family",
    "session_id",
    "result",
    "sealed",
    "reads",
)
MODES = {"decide", "review", "synthesize"}
DEPTHS = {"quick", "standard", "deep"}
STATUSES = {"complete", "partial", "abstained"}
LEVELS = {"L0", "L1", "L2", "imported"}
FINAL_SHAPES = {
    "decide": (
        "## Recommendation",
        "## Why",
        "## Next action",
        "## Risks and safeguards",
        "## What would change the recommendation",
        "## Confidence",
        "## Material dissent",
        "## Coverage and limitations",
    ),
    "review": (
        "## Verdict",
        "## Prioritized findings",
        "## Recommended changes",
        "## Next validation step",
        "## Strengths to preserve",
        "## Risks and safeguards",
        "## What would change the verdict",
        "## Confidence",
        "## Material dissent",
        "## Coverage and limitations",
    ),
    "synthesize": (
        "## Combined conclusion",
        "## Why",
        "## Implications and next action",
        "## Irreducible differences",
        "## What would change the conclusion",
        "## Confidence",
        "## Material dissent",
        "## Coverage and limitations",
    ),
}


def read_manifest(run_dir: Path) -> tuple[dict | None, str | None]:
    manifest_path = run_dir / "manifest.json"
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, f"unreadable manifest.json: {error}"
    if not isinstance(data, dict):
        return None, "manifest.json must contain a JSON object"
    return data, None


def safe_artifact(run_dir: Path, value: object) -> tuple[Path | None, str | None]:
    if not isinstance(value, str) or not value:
        return None, "artifact path must be a non-empty string"
    candidate = Path(value)
    if candidate.is_absolute() or PureWindowsPath(value).is_absolute():
        return None, "artifact path escapes run directory"
    resolved = (run_dir / candidate).resolve()
    try:
        resolved.relative_to(run_dir.resolve())
    except ValueError:
        return None, "artifact path escapes run directory"
    return resolved, None


def fence_marker(line: str) -> tuple[str, int, str] | None:
    stripped = line.lstrip(" ")
    if len(line) - len(stripped) > 3 or not stripped:
        return None
    marker = stripped[0]
    if marker not in {"`", "~"}:
        return None
    length = len(stripped) - len(stripped.lstrip(marker))
    if length < 3:
        return None
    remainder = stripped[length:]
    if marker == "`" and marker in remainder:
        return None
    return marker, length, remainder


def level_two_headings(markdown: str) -> tuple[str, ...]:
    headings: list[str] = []
    active_fence: tuple[str, int] | None = None
    for line in markdown.splitlines():
        marker = fence_marker(line)
        if active_fence is not None:
            if (
                marker is not None
                and marker[0] == active_fence[0]
                and marker[1] >= active_fence[1]
                and not marker[2].strip()
            ):
                active_fence = None
            continue
        if marker is not None:
            active_fence = marker[0], marker[1]
            continue
        if line.startswith("## "):
            headings.append(line)
    return tuple(headings)


def validate(manifest: dict, run_dir: Path) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in manifest:
            errors.append(f"missing required field: {field}")

    if manifest.get("schema_version") != "1.0":
        errors.append(f"invalid schema_version: {manifest.get('schema_version')}")
    if not isinstance(manifest.get("run_id"), str) or not manifest.get("run_id"):
        errors.append("invalid run_id")
    if manifest.get("mode") not in MODES:
        errors.append(f"invalid mode: {manifest.get('mode')}")
    if manifest.get("depth") not in DEPTHS:
        errors.append(f"invalid depth: {manifest.get('depth')}")
    if manifest.get("status") not in STATUSES:
        errors.append(f"invalid status: {manifest.get('status')}")
    if manifest.get("independence_level") not in LEVELS:
        errors.append(f"invalid independence_level: {manifest.get('independence_level')}")
    if not isinstance(manifest.get("failures"), list):
        errors.append("failures must be a list")

    perspectives = manifest.get("perspectives")
    imports = manifest.get("imports", [])
    imports_valid = isinstance(imports, list) and bool(imports)
    if not isinstance(perspectives, list):
        errors.append("perspectives must be a list")
        perspectives = []
    elif not perspectives and not (manifest.get("mode") == "synthesize" and imports_valid):
        errors.append("perspectives must be a non-empty list")
    if "imports" in manifest and not isinstance(imports, list):
        errors.append("imports must be a list")
        imports = []

    artifact_fields: list[tuple[str, object, int | None]] = [
        (field, manifest.get(field), None)
        for field in ("brief", "context_manifest", "challenge", "fusion", "final")
    ]
    artifact_fields.extend(("imports", item, None) for item in imports)
    for index, perspective in enumerate(perspectives):
        if not isinstance(perspective, dict):
            errors.append(f"perspective {index} must be an object")
            continue
        if set(perspective) != set(PERSPECTIVE_FIELDS):
            errors.append(f"invalid perspective fields: {index}")
        if not isinstance(perspective.get("id"), str) or not perspective.get("id"):
            errors.append(f"invalid perspective id: {index}")
        if not isinstance(perspective.get("executor"), str) or not perspective.get("executor"):
            errors.append(f"invalid perspective executor: {index}")
        for field in ("model_family", "session_id"):
            if not isinstance(perspective.get(field), str):
                errors.append(f"invalid perspective {field}: {index}")
        if not isinstance(perspective.get("sealed"), bool):
            errors.append(f"invalid perspective sealed: {index}")
        reads = perspective.get("reads")
        if not isinstance(reads, list):
            errors.append(f"perspective reads must be a list: {index}")
            reads = []
        artifact_fields.append(("result", perspective.get("result"), index))
        artifact_fields.extend(("reads", read, index) for read in reads)

    final_path: Path | None = None
    resolved_results: dict[int, Path] = {}
    resolved_reads: list[tuple[int, Path]] = []
    for field, value, perspective_index in artifact_fields:
        artifact, error = safe_artifact(run_dir, value)
        if error:
            errors.append(error)
            continue
        if not artifact.is_file():
            errors.append(f"missing artifact: {value}")
        if field == "final":
            final_path = artifact
        elif field == "result" and perspective_index is not None:
            resolved_results[perspective_index] = artifact
        elif field == "reads" and perspective_index is not None:
            resolved_reads.append((perspective_index, artifact))

    if manifest.get("independence_level") in {"L1", "L2"}:
        for perspective_index, read in resolved_reads:
            peer_results = {
                result
                for peer_index, result in resolved_results.items()
                if peer_index != perspective_index
            }
            if read in peer_results:
                errors.append("peer result read before fusion")

    if final_path is not None and final_path.is_file():
        try:
            final_text = final_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            errors.append(f"unreadable final.md: {error}")
        else:
            expected_headings = FINAL_SHAPES.get(
                manifest.get("mode"), FINAL_SHAPES["decide"]
            )
            lines = final_text.splitlines()
            first_nonblank = next((line for line in lines if line.strip()), "")
            if first_nonblank != expected_headings[0]:
                errors.append(f"final.md must begin with {expected_headings[0]}")

            actual_headings = level_two_headings(final_text)
            missing_headings = [
                heading for heading in expected_headings if heading not in actual_headings
            ]
            for heading in missing_headings:
                errors.append(f"missing final section: {heading.removeprefix('## ')}")
            if not missing_headings and actual_headings != expected_headings:
                errors.append("final sections are not in canonical order")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: validate_run.py RUN_DIRECTORY", file=sys.stderr)
        return 2
    run_dir = Path(argv[0])
    if not run_dir.is_dir():
        print(f"unreadable run directory: {run_dir}", file=sys.stderr)
        return 2
    manifest, error = read_manifest(run_dir)
    if error:
        print(error, file=sys.stderr)
        return 2
    errors = validate(manifest, run_dir)
    for error in errors:
        print(error, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
