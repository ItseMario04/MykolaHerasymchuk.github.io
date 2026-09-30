import argparse
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = ROOT / "Python_code"
POLL_INTERVAL = 1
STABLE_SECONDS = 1


def notebooks():
    return sorted(NOTEBOOK_DIR.glob("*.ipynb"))


def signature(path):
    stat = path.stat()
    return stat.st_mtime_ns, stat.st_size


def export_notebook(path):
    subprocess.run(
        [
            sys.executable,
            "-m",
            "nbconvert",
            "--to",
            "html",
            "--HTMLExporter.embed_images=True",
            "--output",
            path.stem + ".html",
            str(path),
        ],
        cwd=ROOT,
        check=True,
    )
    print("Exported " + str(path.relative_to(ROOT)), flush=True)


def build_all():
    for path in notebooks():
        html_path = path.with_suffix(".html")
        if not html_path.exists() or html_path.stat().st_mtime_ns < path.stat().st_mtime_ns:
            export_notebook(path)


def watch():
    print("Notebook watcher starting", flush=True)
    build_all()
    exported = {path: signature(path) for path in notebooks()}
    pending = {}
    print("Notebook watcher ready", flush=True)

    while True:
        now = time.monotonic()
        current_paths = set(notebooks())

        for deleted_path in set(exported) - current_paths:
            exported.pop(deleted_path, None)
            pending.pop(deleted_path, None)

        for path in current_paths:
            try:
                current_signature = signature(path)
            except FileNotFoundError:
                continue

            if current_signature == exported.get(path):
                pending.pop(path, None)
                continue

            previous = pending.get(path)
            if previous is None or previous[0] != current_signature:
                pending[path] = current_signature, now
                continue

            if now - previous[1] < STABLE_SECONDS:
                continue

            try:
                export_notebook(path)
            except subprocess.CalledProcessError as error:
                print("Export failed for " + path.name + ": " + str(error), flush=True)
            else:
                exported[path] = current_signature
            pending.pop(path, None)

        time.sleep(POLL_INTERVAL)


def main():
    parser = argparse.ArgumentParser(description="Export saved Jupyter notebooks to static HTML.")
    parser.add_argument("--watch", action="store_true", help="watch Python_code for added or changed notebooks")
    args = parser.parse_args()

    if args.watch:
        watch()
    else:
        build_all()


if __name__ == "__main__":
    main()