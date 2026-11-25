"""Entry for make.fun bounty "Make the AI Judge Laugh".

One line about office life: the printer that has been "warming up" since
Tuesday. The joke is built on the laugh recipe — a relatable scene, one
specific named detail, and an absurd closer in the last beat:

  1. Relatable scene: the office printer stuck warming up.
  2. Specific detail: "since Tuesday", and IT's "give it a minute".
  3. Absurd closer: the printer has now outlasted two interns and a
     marriage — the machine's uptime beats human milestones.

Delete the last sentence and the joke loses its meaning: the escalation
is the punchline, not decoration. 128 characters, under the 200 cap.
"""

from pathlib import Path

TEXT = "The office printer has been warming up since Tuesday. IT says give it a minute. It has now outlasted two interns and a marriage."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip(), "entry must not be whitespace only"
    return size


def check_gate(text):
    """Mirror the bounty gate: UTF-8, 1-200 chars, not whitespace only."""
    text.encode("utf-8")
    return check_len(text)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_gate(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
