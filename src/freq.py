import matplotlib.pyplot as plt
import util

EXAMPLE_CIPHERTEXT = """
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


def freq_map(text: str) -> dict[str, int]:
    text.lower()
    map = dict()
    for alph in util.ALPHABET:
        map[alph] = 0
    for char in text:
        freq = map.get(char)
        if freq != None:
            freq = freq + 1
            map[char] = freq

    return map


def graph_freq_map(map: dict[str, int], show_heights=True):
    y = [*map.values()]
    x = [*map.keys()]
    plt.title("Frequency Counts of Text")
    plt.bar(x, y, width=0.5)
    plt.xlabel("Character")
    plt.ylabel("Occurences in Text")
    if show_heights:
        for index, value in enumerate(y):
            plt.text(index - 0.25, value + 0.4, str(value))

    plt.show()


def main():
    map = freq_map(EXAMPLE_CIPHERTEXT)
    graph_freq_map(map)


if __name__ == "__main__":
    main()
