#!/usr/bin/env python3
"""
Milestone 4 calibration: print both signals and the combined score, side by side.

    python calibrate.py

Runs the same pipeline as POST /submit (minus the web route and the log), so
you can see which signal is responsible when a combined score surprises you.

Paste your four inputs below. Keep them roughly the same length
(150-300 words each): the word-variety measure drops as text gets longer,
so inputs of very different lengths will differ on that measure for a
reason that has nothing to do with who wrote them.
"""

import detector
import scoring
import stylometry

INPUTS = {
    "clearly AI": """Artificial intelligence is rapidly transforming the way organizations operate across a wide range of industries. By automating repetitive tasks, AI enables employees to focus on more strategic and creative work. Additionally, machine learning models can analyze large volumes of data to identify patterns and generate valuable insights that support better decision-making. However, the adoption of these technologies also raises important ethical considerations. Organizations must ensure that their AI systems are transparent, fair, and accountable to the people they affect. Furthermore, it is essential to invest in training programs that help employees develop the skills needed to work effectively alongside these tools. Data privacy is another key concern, as AI systems often rely on sensitive personal information. By addressing these challenges proactively, businesses can build trust with customers and stakeholders. Ultimately, the successful integration of AI depends on balancing innovation with responsibility, ensuring that technological progress benefits both organizations and society as a whole..""",
    "clearly human": """try not to use too much jargon that is very specific to the field, like still be detailed but make it easy to follow from anyone who is looking at your resume, the sentence structure for example on the first bullet has a lot of info but not very clear to understand , it shouldnt take 2-3 times of rereading the entry to understand what you do is what i mean, another thing, simple is better but be strategic with it. for example, instead of “built an automated prototype,” say “automated the processes of xyz”automating is a good skill. lead with it, second job entry needs a lot of work — “cut a deal” is too informal and sounds weird""",
    "formal human": """ Live with out fear, and you will be free. Fear is the mind killer. Fear is the little death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.""",
    "lightly-edited AI": """death is part of life, and it is a natural process that we all must face. It is important to remember that death is not the end, but rather a transition to another state of being. While it can be difficult to come to terms with the loss of a loved one, it is important to cherish the memories and experiences that we shared with them. In many cultures, death is seen as a celebration of life, and it is common to hold ceremonies and rituals to honor the deceased. It is also important to take care of ourselves during times of grief, and to seek support from friends, family, or professionals if needed. Ultimately, death is a reminder of the preciousness of life, and it encourages us to live fully and appreciate the time we have with those we love.""",
}
    # The detector.py docstring suggests adding this one. It is the writer
    # your system is most likely to accuse.
    # "plain human": "PASTE a plainly written human paragraph.",



def main():
    rows = []
    for name, text in INPUTS.items():
        if text.startswith("PASTE"):
            print(f"skipping '{name}': still the placeholder")
            continue
        model = detector.model_signal(text)
        style = stylometry.style_signal(text)
        combined = round(scoring.combine_signals(model, style), 4)
        guess, _ = scoring.score_to_label(combined)
        rows.append((
            name,
            len(stylometry.words(text)),
            stylometry.sentence_length_spread(text),
            stylometry.type_token_ratio(text),
            model,
            style,
            combined,
            abs(model - style),
            guess,
        ))

    if not rows:
        print("Nothing to score. Paste your texts into INPUTS first.")
        return

    header = (f"{'input':<20}{'words':>6}{'spread':>8}{'TTR':>7}"
              f"{'model':>8}{'style':>8}{'combined':>10}{'gap':>7}  guess")
    print()
    print(header)
    print("-" * len(header))
    for name, n, spread, ttr, model, style, combined, gap, guess in rows:
        print(f"{name:<20}{n:>6}{spread:>8.3f}{ttr:>7.3f}"
              f"{model:>8.4f}{style:>8.4f}{combined:>10.4f}{gap:>7.3f}  {guess}")

    print("\ngap = |model - style|. The biggest gap is your 'signals split' case.")
    for name, label_range in scoring.label_ranges():
        print(f"  {name:<22} {label_range}")


if __name__ == "__main__":
    main()