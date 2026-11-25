"""Write the competition entry: one sentence that could have replaced
an entire pointless meeting, to /output/entry.txt."""

import os

ENTRY = (
    # One sentence, plain office English, no setup: the decision is made,
    # it is written down, and the meeting exists only because nobody read it.
    "It's already decided, it's already in the document, and the only "
    "reason we're still sitting here is that nobody read the document."
)


def main():
    entry = ENTRY.strip()
    if not entry or len(entry) > 200:
        raise SystemExit("entry fails gate: must be 1-200 characters")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry fails gate: must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
