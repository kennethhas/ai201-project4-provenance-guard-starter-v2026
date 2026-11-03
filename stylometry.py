"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """Sample standard deviation divided by mean sentence length."""
    lengths = [
        len(words(sentence))
        for sentence in sentences(text)
        if words(sentence)
    ]

    if len(lengths) < 2:
        return 0.0

    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """Unique words divided by total words."""
    tokens = words(text)

    if not tokens:
        return 0.0

    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    """Selected punctuation characters divided by all characters."""
    if not text:
        return 0.0

    punctuation = set(".,!?;:-—–()[]{}\"'…")
    count = sum(character in punctuation for character in text)
    return count / len(text)


def style_signal(text: str) -> float:
    """Experimental style score: higher means more AI-like."""
    tokens = words(text)
    usable_sentences = [
        sentence for sentence in sentences(text)
        if words(sentence)
    ]

    if len(tokens) < 20 or len(usable_sentences) < 2:
        return 0.5

    spread = sentence_length_spread(text)
    uniformity = 1.0 - min(spread, 1.0)
    repetition = 1.0 - type_token_ratio(text)

    score = (uniformity + repetition) / 2.0
    return round(score, 4)


# ── Combining them ───────────────────────────────────────────────────────────
"""def style_signal(text: str) -> float:
  
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
  
    # TODO: replace this
    return 0.5  """


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")

