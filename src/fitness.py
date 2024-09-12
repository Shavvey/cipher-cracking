from util import ALPHABET
from math import log

import re

PATTERN = re.compile(r"[\W_]+", re.UNICODE)

ENGLISH_TEXT = """
It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their
first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal
secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station
with enough power to destroy an entire planet. Pursued by the Empire's sinister agents,
Princess Leia races home aboard her starship, custodian of the stolen plans that can save her
people and restore freedom to the galaxy. It is a dark time for the Rebellion. Although the
Death Star has been destroyed, Imperial troops have driven the Rebel forces from their
hidden base and pursued them across the galaxy. Evading the dreaded Imperial
Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base
on the remote ice world of Hoth. The evil lord Darth Vader, obsessed with finding young
Skywalker, has dispatched thousands of remote probes into the far reaches of space. Luke
Skywalker has returned to his home planet of Tatooine in an attempt to rescue his friend Han
Solo from the clutches of the vile gangster Jabba the Hutt
"""


def get_textragrams(text: str) -> list[float]:
    text = text.lower()
    text = PATTERN.sub("", text)
    # get rid of spaces new lines and any punctuation
    tetrafreq = [0.00] * 26 * 26 * 26 * 26
    for i in range(len(text) - 3):
        x = (
            ALPHABET.index(text[i]) * 26 * 26 * 26
            + ALPHABET.index(text[i + 1]) * 26 * 26
            + ALPHABET.index(text[i + 2]) * 26
            + ALPHABET.index(text[i + 3])
        )
        tetrafreq[x] += 1
    for i in range(26 * 26 * 26 * 26):
        tetrafreq[i] = tetrafreq[i] / (len(text) - 3)
    return tetrafreq


def fitness(text) -> float:
    tetrafreq = get_textragrams(ENGLISH_TEXT)
    text = text.lower()
    text = PATTERN.sub("", text)
    result = 0
    for i in range(len(text) - 3):
        tetragram = text[i : i + 4]
        x = (
            ALPHABET.index(tetragram[0]) * 26 * 26 * 26
            + ALPHABET.index(tetragram[1]) * 26 * 26
            + ALPHABET.index(tetragram[2]) * 26
            + ALPHABET.index(tetragram[3])
        )
        y = tetrafreq[x]
        if y == 0:
            result += -15  # some large negative number
        else:
            result += log(y)
    result = result / (len(text) - 3)
    return result
