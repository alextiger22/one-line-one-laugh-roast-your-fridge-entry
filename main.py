#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — entry program.

Writes a single roast line to /output/entry.txt, then reads it back
and self-verifies the gate (UTF-8, 1-200 chars, not only whitespace).
"""

import os

LINE = "My fridge hums all night like it's working a double shift, yet the ice maker has been on strike since 2019 and the freezer is just where bread goes to die."


def validate(line):
    """Check the judge's gate before writing: UTF-8, 1-200 chars,
    not only whitespace, and roasts a fridge or a phone."""
    line.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8
    assert 1 <= len(line) <= 200, f"length {len(line)} out of gate"
    assert line.strip(), "entry is only whitespace"
    lowered = line.lower()
    assert "fridge" in lowered or "phone" in lowered, (
        "entry must roast a fridge or a phone"
    )
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back self-verification
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    validate(back)
    print(f"entry ({len(back)} chars): {back}")


if __name__ == "__main__":
    main()
