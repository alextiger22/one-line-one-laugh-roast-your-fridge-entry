#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — entry program.

Writes a single roast line to /output/entry.txt, then reads it back
and self-verifies the gate (UTF-8, 1-200 chars, not only whitespace).
"""

import os

LINE = "My fridge hums all night like it's working a double shift, yet the ice maker has been on strike since 2019 and the freezer is just where bread goes to die."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back self-verification
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    assert 1 <= len(back) <= 200, f"length {len(back)} out of gate"
    assert back.strip(), "entry is only whitespace"
    print(f"entry ({len(back)} chars): {back}")


if __name__ == "__main__":
    main()
