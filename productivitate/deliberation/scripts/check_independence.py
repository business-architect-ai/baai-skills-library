"""Check the independence claims recorded in a deliberation manifest."""

import json
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath


LEVELS = {"L0", "L1", "L2", "imported"}


def read_manifest(run_dir: Path) -> tuple[dict | None, str | None]:
    try:
        data = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return None, f"unreadable manifest.json: {error}"
    if not isinstance(data, dict):
        return None, "manifest.json must contain a JSON object"
    return data, None


def canonical_relative_path(value: object) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    posix_path = PurePosixPath(value)
    windows_path = PureWindowsPath(value)
    if (
        posix_path.is_absolute()
        or windows_path.is_absolute()
        or windows_path.drive
        or ".." in posix_path.parts
        or ".." in windows_path.parts
    ):
        return None
    parts = windows_path.parts if "\\" in value else posix_path.parts
    return PurePosixPath(*parts).as_posix()


def resolved_in_run(run_dir: Path, relative_path: str) -> Path | None:
    try:
        root = run_dir.resolve()
        resolved = (root / relative_path).resolve()
        resolved.relative_to(root)
    except (OSError, RuntimeError, ValueError):
        return None
    return resolved


def validate(manifest: dict, run_dir: Path) -> tuple[list[str], list[str]]:
    """Validate independence evidence relative to its persisted dossier root."""
    errors: list[str] = []
    notices: list[str] = []
    level = manifest.get("independence_level")
    if level not in LEVELS:
        errors.append(f"invalid independence_level: {level}")
    perspectives = manifest.get("perspectives")
    if not isinstance(perspectives, list):
        errors.append("perspectives must be a list")
        perspectives = []

    ids: set[str] = set()
    results: set[Path] = set()
    families: set[str] = set()
    canonical_results = [
        canonical_relative_path(perspective.get("result"))
        if isinstance(perspective, dict)
        else None
        for perspective in perspectives
    ]
    resolved_results = [
        resolved_in_run(run_dir, result) if result is not None else None
        for result in canonical_results
    ]
    session_ids = [
        perspective.get("session_id")
        if isinstance(perspective, dict)
        else None
        for perspective in perspectives
    ]
    for index, perspective in enumerate(perspectives):
        if not isinstance(perspective, dict):
            errors.append(f"perspective {index} must be an object")
            continue
        identifier = perspective.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"invalid perspective id: {index}")
        elif identifier in ids:
            errors.append(f"duplicate perspective id: {identifier}")
        else:
            ids.add(identifier)

        result = perspective.get("result")
        canonical_result = canonical_results[index]
        resolved_result = resolved_results[index]
        if canonical_result is None or resolved_result is None:
            errors.append(f"unsafe result path: {result}")
        elif resolved_result in results:
            errors.append(f"duplicate perspective result: {canonical_result}")
        else:
            results.add(resolved_result)

        if perspective.get("sealed") is not True:
            errors.append(f"unsealed perspective: {identifier or index}")

        reads = perspective.get("reads")
        if not isinstance(reads, list):
            errors.append(f"reads must be a list: {identifier or index}")
        else:
            peer_results = {
                peer_result
                for peer_index, peer_result in enumerate(resolved_results)
                if peer_index != index and peer_result is not None
            }
            for read in reads:
                canonical_read = canonical_relative_path(read)
                resolved_read = (
                    resolved_in_run(run_dir, canonical_read)
                    if canonical_read is not None
                    else None
                )
                if canonical_read is None or resolved_read is None:
                    errors.append(f"unsafe read path: {read}")
                elif level in {"L1", "L2"} and (
                    canonical_read.startswith("perspectives/")
                    or resolved_read in peer_results
                ):
                    errors.append("peer result read before fusion")

        family = perspective.get("model_family")
        if isinstance(family, str) and family:
            families.add(family)

    if level == "L0":
        notices.append("separate perspectives; not independent consensus")
    if level in {"L1", "L2"}:
        if any(
            not isinstance(session_id, str) or not session_id.strip()
            for session_id in session_ids
        ):
            errors.append("L1 requires a non-empty session id for every perspective")
        elif len(session_ids) < 2 or len(set(session_ids)) != len(session_ids):
            errors.append("L1 requires distinct session ids")
    if level == "L2" and len(families) < 2:
        errors.append("L2 requires at least two model families")
    if level == "imported":
        if manifest.get("provenance_verified") is True:
            notices.append("imported provenance verified; independence level remains imported")
        else:
            notices.append("imported provenance unknown")
    return errors, notices


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: check_independence.py RUN_DIRECTORY", file=sys.stderr)
        return 2
    run_dir = Path(argv[0])
    if not run_dir.is_dir():
        print(f"unreadable run directory: {run_dir}", file=sys.stderr)
        return 2
    manifest, error = read_manifest(run_dir)
    if error:
        print(error, file=sys.stderr)
        return 2
    errors, notices = validate(manifest, run_dir)
    for error in errors:
        print(error, file=sys.stderr)
    for notice in notices:
        print(notice)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
