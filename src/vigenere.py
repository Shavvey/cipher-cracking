from numpy import copy


def vig_encryption(key: int, plaintext: str) -> str:
    ciphertext = copy(plaintext)
    for c in ciphertext:
        
