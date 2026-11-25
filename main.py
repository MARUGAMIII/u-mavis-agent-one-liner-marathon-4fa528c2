#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original deadpan one-line joke to /output/entry.txt.

Candidates considered (all original, written for this entry):
  1. "I bought noise-canceling headphones so I could hear myself think,
      and it turns out I think mostly in grocery lists."
  2. "I told my landlord the faucet drips in Morse code, and now he thinks
      the apartment is haunted by a plumber."
  3. "I bought a plant to prove I could keep something alive, and now we
      both just sit there disappointed in each other."
  4. "I asked the barista for something that tastes like a Tuesday and she
      handed me a decaf and said, exactly."

Revision 1: candidate 2 was good but its punchline ("haunted by a plumber")
only restated the setup. The sharper turn is the landlord MONETISING the
haunting: he does not fix the faucet, he charges extra rent for the ghost
plumber. That adds a second surprise (greedy landlord) on top of the first
(Morse-code faucet), keeps the deadpan voice, and lands in one read.

Revision 2: "charges extra rent" was good, but "charges ME extra rent"
is sharper — the victim is the speaker, which makes the landlord's greed
land harder and gives the line a clearer point of view. One word, one
extra beat of deadpan injustice. Final length 106 chars, still plain
ASCII, no em dash.
"""

import os

JOKE = (
    "I told my landlord the faucet drips in Morse code, and now he charges "
    "me extra rent for the ghost plumber."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.isascii(), "joke must be plain ASCII"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
