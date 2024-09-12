from util import ALPHABET


def index_of_coincidence(text: str):
    counts = [0] * 26
    for char in text:
        counts[ALPHABET.index(char)] += 1
    numer = 0
    total = 0
    for i in range(26):
        numer += counts[i] * (counts[i] - 1)
        total += counts[i]
    return 26 * numer / (total * (total - 1))


def ioc(ciphertext: str) -> float | None:
    found = False
    period = 0
    while not found:
        period += 1
        slices = [""] * period
        for i in range(len(ciphertext)):
            slices[i % period] += ciphertext[i]
        sum = 0
        for i in range(period):
            sum += index_of_coincidence(slices[i])
        ioc = sum / period
        if ioc > 1.6:
            found = True
            return ioc
