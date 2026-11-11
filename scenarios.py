"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""
"""Fixed inputs for the five Unit 8 criteria."""

# Supplied by Kenneth from his own writing.
# Some samples contain quotations. Samples 7–9 are related excerpts.
HUMAN_TEXTS = [
    # 1
    """In International news, being the number one problem in Ukraine’s corruption has come to the limit. corruption in countries can have lots of trouble making every one’s life is miserable mostly the citizen who pays taxes. But not to the corruptor as the only seeking what they desire and putting danger to the citizen. Even with the punishment for doing crime that corrupt practices are rarely serious punished. Consider the constitutional court ruled those who accused for corruption has also corrupted showing that the country has become a corrupt country.

Corruption in the government came from egotistical, being selfish only concerned with its self-interest. Government corruption presented in Measure for Measure by William Shakespeare. Shakespeare uses the character to show how one being egotistical can cause to corruption. With overly concerned with one own desire or needs one willing to do dirty technique to achieve its goal and shows corruption in the government came from egotistical. Some believe that corruption was innated in humanity and considering that we live in a society of self-centered people. To achieve something or to reach their goal many humanities will use illegal action to achieve it. As corruption government came from egotistical.""",

    # 2
    """The founding mothers of the United States Feminist movement understood that the battle for quality would be long and hard. They understood that they may not be able to win in a battle of arms and formulated a long-term plan for women’s equality. They believed that the way to do this was to link less women’s rights to accepted norms in the United States and slowly bridge the gap between the understandable and far-fetched reforms of the women’s rights movement.

Women at the time of the Declaration had very little rights. Unmarried women had some rights but once they were married all their rights went to their husbands. They did not have the right to vote and  their rights varied greatly by state. There was no unifying body to help or protect women. The Seneca Fall’s Convention started as a band of women who were fed up with the system and led to an idealogical revolution, causing the entire country to question how the social stratification of the entire United States.

The Declaration of Sentiments is quintessential example of the synthesis of conventional and radical. Using the Declaration of Independence as an outline, the authors were able to convey that women’s rights were just like the right to revolt, to some it may seem outlandish and preposterous but is “in the course of Human events” (Stanton), the normal way of the world.  The Declaration of Sentiment was ratified by the Seneca Falls Convention in 1848 by delegates who disagreed on the exact path to take but all agreed that the status quo of women in the United States must change.""",

    # 3
    """Every Saturday, the Al-Hikmah mosque also offers Saturday School, where elementary and middle school students can learn more about Islam religion. This Saturday School was held after I cleaned the mosque. I kept on watch during Saturday School because the most common problem is the mic problem. Besides, I helped the teacher teach lessons to the students and while help teaching, I also learned about the lessons during Saturday School. Saturday School is usually an hour or more because it depends on the teacher and the lesson he or she taught. After the Saturday School was done, I helped turn off the stuff like mics and sound system used during the Saturday School and other stuff like small tables and put them back to the utility room. It took me half an hour or more to get it done. Those are the last activities I did during my community service. At last, community service is enjoyable for me and I felt good about myself for being a volunteer because it is very beneficial for me, the mosque administrator, and those students. I earned a beneficial experience in doing this community service.""",

    # 4
    """In the prologue from Romeo and Juliet  buy william shakespeare the author utilize tone to convey the idea that hatred can lead to violence and death

from the text the author utilize of tone to help the audience  to understand the speaker's attitude toward the story .The tragic from shakespeare word that support the central idea that hatred can lead to violence and death. Example in line 4 shakespeare write “ where civil blood makes civil hands unclean.”the words unclean means causing death. That informs the reader that there will be a tragedy. And the words civil bloods means hatred . that informs there is anger in this story. in line 8 “Doth with their death bury their parents’ strife.“the word “parent strife it means that their parents heatered” and the word “their Death “ means the lover death . Final “ parent rage means that their parent heaterd  was causing  them their death.

thus. it is evident that shakespeare utilize tone to clarify develops the tragic and melancholy for the lovers and point out that hatred can lead to violence and death""",

    # 5
    """In the song who knows from west side story by stephen sondheim  uses rhyme to help the listener to convey the idea that hope can lead to to confidence

In the text who knows the author use rhyme to help the listener to understand the singer toward the story. For example in stanza 3&4 “There something due any day I will know right away” illustrate of confidence . this can be interpreted to mean that he is very confidence that there is something great will come to him . The words “I will know right away” mean  that  he is very sure that there is gonna be great will happen to him. In addition the following line “I got a feeling there is a miracle due , gonna come true” from stanza 1 means he believed that something good is coming . it represent confidence

Therefore, it is evident that the author stephen sondheim uses rhyme to developes the confident and point out that hope leads to confidence""",

    # 6
    """In the lyrics the writer uses tone to help the listener to understand the performance attitude toward  the story one can infer the brotherhood tone from stephen sondheim that the central idea people join gang for fellowship & brotherhood , example in the lyrics line 3-4 “from your first cigarette To your last dyin’ day.”that can infer to that when they join the gang from a young age they will be in the gang until his dying age . In other words his loyalty to the gang . In other lyrics in line 18-19 “when you are a jet you stay a jet” it can be illustrated that once you are in this family wherever you go you will be already in this family""",

    # 7
    """I suppose once you mature, there would be a lot of things that you said when you were younger that you now would disagree with. When I was in class, one of my friends kept saying that what we learned in high school is worthless. We were not going to use it any way in the future; nothing we do in high school is needed to work. I didn’t really think about it and just nodded along despite not knowing what exactly he meant. But in times when a person repeatedly hears the same thing from people it really makes you think: is what I’m doing right now a waste of time?  It was on my mind for a couple weeks until I reflected on my experience in middle school.""",

    # 8
    """Now, I understand that those garbage that seems worthless had a lot of nutrients in them that can be used for the tree to grow. In the same way, in that seemingly worthlessness of high school that my friend said, you can gain experiences to grow and produce sweet fruits of labor. In high school you don’t only learn from text books, but also from the people around you. You may not see the result now, but it will definitely come, like the mango tree that needed 4 years to grow and produce fruits.""",

    # 9
    """Not only in high school, I believe that everything I have ever done was never meaningless or worthless. The journey that I will take can be hard or arduous, but it will never be worthless to me. Albert Einstein tells us that the only source of knowledge is experience. By knowing that, everything I am going to do in the future will never be worthless to me for gaining more experience. I hope to continue to gain more experience through both my successes and failures.""",

    # 10
    """Classics do not stop influencing readers when they finish reading because they will always be able to relate and reflect to the present. The short story “The Most Dangerous Game” by Richard Connell, depicts a man named Rainford that is at the mercy of a human’s hunter who forces him to play a game that will determine his fate: life or death. As we gather life experience we see more in classics “The Most Dangerous Game” can relate to the present by showing that in real life stronger will survive.""",
]

# Generated in this conversation for the label-coverage test.
AI_TEXTS = [
    """Learning is a gradual process that requires patience and consistent effort. Students develop knowledge by reviewing information, practicing skills, and reflecting on mistakes. Although progress may not be immediately visible, regular practice can lead to meaningful improvement. Challenges provide opportunities to identify weaknesses and develop better strategies. Over time, these experiences help students become more confident and independent learners.""",

    """Community service provides benefits for both volunteers and the people they support. Volunteers contribute their time and effort to activities that address local needs. These activities may include organizing supplies, maintaining shared spaces, or assisting educational programs. Through participation, volunteers can develop communication skills and gain practical experience. Consistent involvement also helps build stronger relationships within the community.""",

    """Effective teamwork depends on clear communication and shared responsibilities. Each team member should understand the overall objective and the tasks assigned to them. Regular updates help the group identify problems before they become more difficult to resolve. When disagreements occur, respectful discussion can help members find a workable solution. A coordinated approach allows the team to make steady progress toward its goal.""",

    """Literature allows readers to explore experiences beyond their own lives. Through characters and conflicts, stories raise questions about loyalty, ambition, and personal responsibility. Readers may interpret the same story differently as they gain experience. A decision that once seemed reasonable may later appear selfish or misguided. This ability to support new interpretations helps older works remain relevant to modern audiences.""",

    """Regular exercise can become easier to maintain when it is part of a consistent routine. Setting manageable goals helps people build habits without taking on too much at once. Tracking progress can also make improvements easier to recognize. Rest and recovery should be considered alongside physical activity. A balanced routine gives people room to adjust their plans as their needs and circumstances change.""",
]

# Kenneth's replacement openings, supplied in this conversation.
EDITED_OPENINGS = [
    "Learning is an essential life skill; it requires time and sacrifice.",
    "Community service can be beneficial not only to the community but to the individual as they grow people skill and develop character",
    "Teamwork can be hard with the mind of a narcissist as they want to help people the most to get the fame or the credit .",
    "creativity and Imagination are key in a child's life, and one way to train them is with literature",
    "Exercise is a part of discipline too; a healthy mind needs a healthy body to stay disciplined. One must have a well built body. So exercise is key to being disciplined",
]

# Replace only the original first sentence.
# A newline separates the supplied opening from the unchanged remainder.
EDITED_TEXTS = [
    opening + "\n" + original.split(". ", 1)[1]
    for opening, original in zip(EDITED_OPENINGS, AI_TEXTS)
]

LABEL_TEXTS = {
    "human": "We think this was most likely written by a person.",
    "unsure": (
        "We couldn’t tell whether a person or AI wrote this. "
        "It could be either."
    ),
    "ai": (
        "Our checks suggest this writing may be AI-generated, "
        "but we could be wrong. You can appeal if you disagree"
    ),
}

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": HUMAN_TEXTS,
    },
    {
        "name": "label coverage",
        "criterion": 2,
        "texts": HUMAN_TEXTS[:5] + AI_TEXTS + EDITED_TEXTS,
    },
    {
        "name": "invalid text",
        "criterion": 4,
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": " ", "creator_id": "eval_bad_spaces"},
            {"text": 123, "creator_id": "eval_bad_number"},
        ],
    },
]


def validate() -> list[str]:
    """Check the test definitions before sending any requests."""
    problems = []

    if [s.get("criterion") for s in SCENARIOS] != [1, 2, 3, 4, 5]:
        problems.append("Expected criteria 1–5, once each and in order.")

    expected_counts = {1: 10, 2: 15, 3: 5, 4: 4, 5: 9}
    expected_kinds = {
        1: "submissions",
        2: "submissions",
        3: "appeals",
        4: "bad_input",
        5: "boundaries",
    }

    for scenario in SCENARIOS:
        number = scenario.get("criterion")
        kind = scenario.get("kind")

        if not scenario.get("name") or not scenario.get("target"):
            problems.append(f"Criterion {number} needs a name and target.")

        if kind != expected_kinds.get(number):
            problems.append(f"Criterion {number} has an unexpected kind.")
            continue

        if kind in ("submissions", "appeals"):
            items = scenario.get("texts", [])
            for i, text in enumerate(items, 1):
                if not isinstance(text, str) or not text.strip():
                    problems.append(
                        f"Criterion {number}, text {i} is not a nonempty string."
                    )
                elif text.startswith("REPLACE ME"):
                    problems.append(
                        f"Criterion {number}, text {i} is still a placeholder."
                    )

            if kind == "submissions":
                if len(scenario.get("sources", [])) != len(items):
                    problems.append(
                        f"Criterion {number} needs a source for every text."
                    )

            if kind == "appeals":
                reasons = scenario.get("reasonings", [])
                if len(reasons) != len(items):
                    problems.append("Each appeal needs its own reasoning.")
                if any(
                    not isinstance(reason, str) or not reason.strip()
                    for reason in reasons
                ):
                    problems.append("Appeal reasoning cannot be empty.")

        elif kind == "bad_input":
            items = scenario.get("bodies", [])
            if any(not isinstance(body, dict) for body in items):
                problems.append("Bad-input bodies must be dictionaries.")

        else:
            items = scenario.get("cases", [])
            for case in items:
                if (
                    not isinstance(case, dict)
                    or not isinstance(case.get("score"), (int, float))
                    or case.get("guess") not in LABEL_TEXTS
                ):
                    problems.append("Invalid boundary-test case.")

        if len(items) != expected_counts[number]:
            problems.append(
                f"Criterion {number} needs {expected_counts[number]} "
                f"inputs; found {len(items)}."
            )

    return problems


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
