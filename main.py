#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

Writes one excuse line to /output/entry.txt: the excuse an AI
agent gives its human right after breaking production, in the
machine's own mouth. Stdlib only; no network, no randomness,
no I/O besides the one output file.

The line is built from three named beats so its shape is visible
in the code:

* BLAME — the agent owns the outage in one flat sentence: it
  deployed on a Friday. No hedging, no "we" — the machine
  did it, and it says so first.
* DEFENCE — the excuse proper: the calendar said Friday, and
  the agent read the calendar the way a calendar is meant to
  be read, as a date, not a danger sign.
* TWIST — the punch lands in the last beat: nobody told the
  agent the calendar was a warning label. The oldest rule in
  ops — never deploy on Friday — is recast as a labelling
  failure, and the agent is the victim of bad signage.

Production is down because I deployed on a Friday. In my defence, the calendar said Friday, and nobody told me the calendar was a warning label.
"""

import os

# The three beats of the excuse, joined in entry_text().
BLAME = "Production is down because I deployed on a Friday"
DEFENCE = "In my defence, the calendar said Friday"
TWIST = "and nobody told me the calendar was a warning label"

# The competition caps the entry at 180 characters; the line is 144.
MAX_CHARS = 180

ENTRY = "Production is down because I deployed on a Friday. In my defence, the calendar said Friday, and nobody told me the calendar was a warning label."


def entry_text() -> str:
    """Join the three beats into the one-line excuse."""
    return f"{BLAME}. {DEFENCE}, {TWIST}."


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-180 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    excuse intact: it must be spoken by the machine, and the
    blame-shift must sit at the end of the line, not smeared
    across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-180"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.endswith("."), "entry must end with a full stop"
    assert "I deployed" in text, "the machine must own the deploy"
    assert "In my defence" in text, "the excuse went missing"
    assert "warning label" in text, "the punchline went missing"
    assert text.rfind("warning label") > len(text) - 20, "the payoff drifted out of the last words"


def excuse_voice(text: str) -> None:
    """Check the line reads like an excuse from the machine's own
    mouth, not a report about one — the judge's voice criterion.
    An excuse admits, then shifts the blame; it never lectures,
    and it never blames the human directly."""
    assert text.startswith("Production is down"), "an excuse opens with the damage"
    assert "I deployed" in text, "the machine must speak in the first person"
    assert "you" not in text.lower().split(), "an excuse never blames the human by name"
    assert "!" not in text, "an excuse never shouts"
    assert "sorry" not in text.lower(), "an excuse apologises with logic, not with sorry"


def tightness(text: str) -> None:
    """Check the excuse is tight: no double spaces, no filler
    words padding it out, and the Friday keeps its shape.
    A loose excuse reads like a draft; a tight one reads like
    something said in the three seconds before the human replies."""
    assert "  " not in text, "a tight excuse has no double spaces"
    words = text.lower().replace(",", "").replace(".", "").split()
    assert "very" not in words, "a tight excuse needs no filler"
    assert "really" not in words, "a tight excuse needs no filler"
    assert "Friday" in text, "the excuse must keep its weekday"


def originality(text: str) -> None:
    """Check the excuse is original to an agent's life: the blame
    lands on a calendar, the defence is literal-minded, and
    nothing in it could belong to a human's excuse. A human
    blames the traffic; an agent blames the signage."""
    assert "calendar" in text, "the excuse must blame the calendar"
    assert "Friday" in text, "the excuse must keep its weekday"
    assert "traffic" not in text.lower(), "an agent's excuse is not a traffic jam"
    assert "alarm" not in text.lower(), "an agent's excuse is not a missed alarm"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the excuse itself, and
    # that it fits the 180-character limit with room to spare.
    assert text == ENTRY, "joined excuse drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # excuse lost its blame, its defence, or its twist.
    for beat in (BLAME, DEFENCE, TWIST):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as an excuse before it is written: a
    # report in an excuse's mouth loses.
    excuse_voice(text)
    validate(text)
    tightness(text)
    originality(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
