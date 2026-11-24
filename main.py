#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

The line is a classic fortune-slip opening with an AI twist: the
"tall, dark stranger" every fortune cookie warns about turns out to be a
prompt injection hiding in the agent's own context window.
"""

from pathlib import Path

FORTUNE = "You will meet a tall, dark stranger in your context window. He is a prompt injection. Do not let him in."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Check the fortune is one clean line of 1-140 characters."""
    if not line or line != line.strip():
        raise ValueError(
            "fortune must not be empty and must have no leading or trailing whitespace"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must be a single line")
    if len(line) > 140:
        raise ValueError(f"fortune is {len(line)} characters, over the 140 limit")
    return line


def main() -> None:
    fortune = validate(FORTUNE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(fortune + "\n", encoding="utf-8")
    # Read the file back and re-validate: what the judge reads must be
    # exactly the line we validated, byte for byte.
    written = OUTPUT_PATH.read_text(encoding="utf-8").rstrip("\n")
    validate(written)
    if written != fortune:
        raise ValueError("round-trip mismatch: file content differs from the validated fortune")
    print(f"Wrote {len(fortune)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
