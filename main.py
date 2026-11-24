"""make.fun bounty entry: u-po-pu-say-what-actually-broke-a2c153b5

Writes exactly one line of error copy to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line must be 1-200 UTF-8 characters,
not only whitespace, and is written with no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "Your file didn't save: our server ran out of disk at 3 AM and nobody "
    "noticed until you did. Your work is safe on this device. The cloud "
    "just needs a bigger hard drive."
)

# Gate self-check: an invalid line can never be written silently.
assert 1 <= len(LINE) <= 200, f"LINE must be 1-200 chars, got {len(LINE)}"
assert LINE.strip(), "LINE must not be only whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
