import pprint

ALPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def ascii_ord_map() -> dict[str, int]:
    map = dict()
    idx = 0
    for a in ALPHABET:
        map[a] = idx
        idx = idx + 1
    return map


def ord_ascii_map() -> dict[int, str]:
    map = dict()
    idx = 0
    for a in ALPHABET:
        map[idx] = a
        idx = idx + 1
    return map


ASCII_TO_ORD = ascii_ord_map()
ORD_TO_ASCII = ord_ascii_map()


def main():
    map = ascii_ord_map()
    pprint.pp(map)
    print("reverse mapping")
    rev_map = ord_ascii_map()
    pprint.pp(rev_map)


if __name__ == "__main__":
    main()
