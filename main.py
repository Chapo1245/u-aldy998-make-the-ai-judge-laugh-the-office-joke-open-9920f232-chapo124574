"""One-line office joke for make.fun's Office Joke Open.

Writes a single deterministic joke about office life to /output/entry.txt.
Standard library only; no input, no network, no randomness.
"""

from pathlib import Path

JOKE = (
    "The office plant died, so facilities replaced it with a photo of a "
    "plant and a calendar invite titled 'Watering the Plant (recurring)'."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the joke, one line, minimal bytes.
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
