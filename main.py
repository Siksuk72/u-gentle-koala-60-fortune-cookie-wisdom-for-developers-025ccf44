#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The line must pass the competition gate: UTF-8 text,
1 to 120 characters, not only whitespace, no trailing newline.
"""

import os

ENTRY_TEXT = "Your lucky numbers are 404, 500, 502. Do not deploy on a Friday."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 120

FORTUNE_PREFIX = "Your lucky numbers"


def validate(text: str) -> str:
    """Check one fortune-cookie line against the competition gate.

    The gate requires UTF-8 text of 1 to 120 characters that is not only
    whitespace and has no trailing newline. A fortune-cookie line also
    reads like a fortune: it opens with a fortune-style lead-in
    ("Your lucky numbers ...") rather than a bare statement.

    Returns the text unchanged when every check passes; raises
    SystemExit with a plain message otherwise.
    """
    if not text or text.strip() == "":
        raise SystemExit("entry text is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if text != text.rstrip("\n"):
        raise SystemExit("entry text must not end with a newline")
    if not text.startswith(FORTUNE_PREFIX):
        raise SystemExit(
            f"entry text must start with {FORTUNE_PREFIX!r} to read "
            "like a fortune cookie"
        )
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main() -> None:
    text = validate(ENTRY_TEXT)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Only the entry file itself gets a chmod, best effort. Never chmod
    # /output: the grader runs as a different uid and chmod on the
    # directory fails with EPERM.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
