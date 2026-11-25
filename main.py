import os

ENTRY = "Gary called a meeting to ask why morale was low, and got fired in it while nobody in the room said a word."

OUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry failed the 1-200 character gate")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
