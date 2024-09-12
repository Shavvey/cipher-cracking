from util import ALPHABET, ASCII_TO_ORD, ORD_TO_ASCII
from math import log
import string

EXAMPLE = """
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


def vig_encrpytion(key: str, plaintext: str) -> str:
    plaintext = plaintext.lower()
    key_length = len(key)
    ciphertext = ""
    idx = 0
    for p in plaintext:
        if p in ALPHABET:
            c_ord = (ASCII_TO_ORD[p] + ASCII_TO_ORD[key[idx % key_length]]) % 26
            ciphertext += ORD_TO_ASCII[c_ord]
            idx += 1
        else:
            ciphertext += p
    return ciphertext


def vig_decryption(key: str, ciphertext: str) -> str:
    ciphertext = ciphertext.lower()
    key_length = len(key)
    plaintext = ""
    idx = 0
    for p in ciphertext:
        if p in ALPHABET:
            c_ord = (ASCII_TO_ORD[p] - ASCII_TO_ORD[key[idx % key_length]]) % 26
            plaintext += ORD_TO_ASCII[c_ord]
            idx += 1
        else:
            plaintext += p
    return plaintext


def get_textragrams(text: str) -> list[float]:
    text = text.lower()
    # get rid of spaces new lines and any punctuation
    text = text.translate(str.maketrans("", "", string.punctuation + "\n" + " "))
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
    tetrafrequencies = get_textragrams(text)
    text = text.lower()
    # get rid of spaces new lines and any punctuation
    text = text.translate(str.maketrans("", "", string.punctuation + "\n" + " "))
    result = 0
    for i in range(len(text) - 3):
        tetragram = text[i : i + 4]
        x = (
            ALPHABET.index(tetragram[0]) * 26 * 26 * 26
            + ALPHABET.index(tetragram[1]) * 26 * 26
            + ALPHABET.index(tetragram[2]) * 26
            + ALPHABET.index(tetragram[3])
        )
        y = tetrafrequencies[x]
        if y == 0:
            result += -15  # some large negative number
        else:
            result += log(y)
    result = result / (len(text) - 3)
    return result


def main():
    e = fitness(vig_encrpytion("hellothere", EXAMPLE))
    print(e)


if __name__ == "__main__":
    main()
