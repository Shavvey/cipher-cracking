from util import ALPHABET, ASCII_TO_ORD, ORD_TO_ASCII


def encrypt(key: int, plaintext: str) -> str:
    plaintext = plaintext.lower()
    ciphertext = ""
    for p in plaintext:
        if p in ALPHABET:
            c_ord = ASCII_TO_ORD[p] + key
            ciphertext += ORD_TO_ASCII[c_ord]
    return ciphertext


def decrypt(key: int, ciphertext: str) -> str:
    ciphertext = ciphertext.lower()
    ciphertext = ""
    for c in ciphertext:
        if c in ALPHABET:
            p_ord = ASCII_TO_ORD[c] - key
            ciphertext += ORD_TO_ASCII[p_ord]
    return ciphertext
