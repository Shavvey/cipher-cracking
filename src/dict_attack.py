import fitness as f
import vigenere as vig

EXAMPLE = """
nuljbibradwibrgijidooqmlmphourpdskhxxe
kiurpsswuguomiqlqnzymhamadcszsoulitadv
xibohkfefevxywgmeehiptgxcwbrwiyroesjbs
gssdxlmlwqhhxiyxnlqajjyhrrauhhefjegeyo
fwnlqkfyalfssdxhmmwiijtiksiydtsdxautzj
bieejunmdevjixtevuyteeubowuofezszegvbm
ecsinixlsjyhmbtuswfhaiqeeafurxqnkypimn
vcukzixywiztkjlyotmhyxteuhyefigdijfhwf
lmzcwiiazeusyrfrassifamwowftsinimslhir
saftfsrtqmupxgahxpqdajcrfhaiqexlzqxkmt
wiijurgdnlqcgklxuejibehifwyrfejuxfdomw
bxrujdugqssdxqmskobeymwhmezdoufhqdlxyf
allinlqyjumsxvwtnsxeslyqqafihiutzulsri
fwliesghykdekinsfhwiohpefygtglkumsrdwi
jeurxhiqiilxiyfojezjdefpsjdoemcxtifjbi
mbtusamsscjpkpjepmeigdyhiilxmyohhhygmu
lyiretzuwsgrlyyvemawbxnivtyjuafsyxacgd
nesigd
"""


def dictionary_attack(ciphertext: str):
    words = open("../words.txt").read().split("\n")
    words.pop()
    key = ""

    for w in words:
        w = w.lower()
        pt = vig.decrypt(w, ciphertext)
        fit = f.fitness(pt)
        print(f"Key: {w}, Fit-Score: {fit}")
        if fit > -14:
            key = w
            break
    if key == "":
        print("Could not find key!")
    else:
        plaintext = vig.decrypt(key, ciphertext)
        print(f"Key: {key}")
        print(f"{plaintext}")


def main():
    dictionary_attack(EXAMPLE)


if __name__ == "__main__":
    main()
