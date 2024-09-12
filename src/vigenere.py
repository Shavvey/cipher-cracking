from util import ALPHABET, ASCII_TO_ORD, ORD_TO_ASCII

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


def encrypt(key: str, plaintext: str) -> str:
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


def decrypt(key: str, ciphertext: str) -> str:
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


def main():
    ciphertext = encrypt("hellothere", EXAMPLE)
    print(f"---CIPHERTEXT---{ciphertext}")
    plaintext = decrypt("hellothere", ciphertext)
    print(f"---PLAINTEXT---{plaintext}")


if __name__ == "__main__":
    main()
