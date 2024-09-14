import fitness as f
import vigenere as vig


EXAMPLE = """
Or glw jwmmaravy, Msq gjmsziq xzm zkeiifa sth glw msxxu. 
Xzm wgvgl oik cmglgcl lseq svv bsvh, svv jeeofmky anw gdwx 
xui xiuk ss xzm vkic. Efl lni Ftazaz ss Kgl ogw usnmjort snmj 
zlr jskw uj glw esziew. Svv Msq wsqv, “Rig xzmjk fr paozz,” 
eah lpwxi jek tamlg. Efl Yuh feo bzgx glw tamlg asa yusq. 
Efl Yuh fihijgxrh lpw rmtll njuq glw lsxoaika. 
Yuh pedtwj xui dqynx Qeq, ifj xui vijqrrwk pw ieypwl Fokux. 
Svv zlrvw esy iiifqfm eah lpwxi jek ugxrvry, bzk jvvkb vgc. 
Nrv Ogj wnmv, “Twz xuijm tk ea ipxstwr mf bzk qvhkb gl xui oilkvf, 
efl dkx vx kmhgvnxw bzk anxwzk lvbq lpw cegija.” 
Sth Tsv usji glw mpveaww ifj wrtszsziq xzm ogxrvk bzgx
jijm mthrv lpw kbcefaw lvbq lpw cegija lneg awzw gfbzw bzk 
iktsvkk. Eah ab ogw fs. Svv Msq gstdkh glw mpveaww Pwgzrr. 
Svv zlrvw esy iiifqfm eah lpwxi jek ugxrvry, bzk wrggvv jel. 
Efl Yuh feal, “Dkx glw esziew mvvkv glw pwgzrrk jw meglwzwj 
xbkwbzkv vrlw gti cpskw, grq pwb lni qvq tsth nthmsx.” 
Eah ab ogw fs. Ywv ieypwl lni qvq tsth Rejbz, 
grq xzm ogxrvk bzgx jijm ygxuijmv zstilpwx lr gstdkh Fisa. 
Sth Tsv asc xuel ql cef kgwv.
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
        if fit > -10.5:
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
