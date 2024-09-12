from util import ALPHABET
import string

EXAMPLE = """
Px td o ilvzsk sq nwopp ney. Vpmse ztrglwstdl, zximrmyr tkvq r lphopb uhwv, lhzp hcg alvmy
jtcgm cmtxvvj lutprjx alp pjbs Krphgetq Xttzvl. Hfcwgn xyi ieeezx, Yisis watsl teeenio ec lairp
zincsm wprrz xz evx Lqgmyi'd fzmpqrxl apldhu, xyi KILEV LAEI, eu ecxcklh jthgp dhtamfr
dmes sgvyxl wshpf mv hvwavzj og lrkmyi awoglx. Gyywfpr uf xyi Lqatfx'z wzrpwepf tniexz,
Tctbvlwj Plml covlw ysti lmctyh yiy welflomg, gbwezrbhr fj alp dhhsie tseyd hahx teu wlgs alv
givtwp ogk vvwascp tkliust xz evx neceec. Te wl h hrvr xtxs yvv kll Vpmsesmfr. Hpescnnl kll
Hplha Zxrv oed msxu hvwavzjsw, Pqgiymlw hkvsgw oegp rkpzvr alp Csulp wsygpd tkvq kllmc
swwkie fhwp lbw wyiwbio evxt etvvwd evx neceec. Pgowprx xoi ocstkiu Mttpcwts
Wkeyjwpsm, h kisbt zq tkliust jtrvmlvj plh mj Znri Jofalwyxy lrw lwelpepwyik e ypk llgiia flds
hu xyi yixzhx pgv avvwo cy Oskl. Alp pjbs pfvk Hlcha Ceuiy, smdslziu apxs qwgkmek fsfyu
Lrcnesopc, vtz hzwweenvxk xysbwlyrl vj iitsep dkvfvw prez hal jrv yilnvxz sw wwenp. Znri
Jofalwyxy lrw yieffglh ks omd scfl tceuie zt Mhxfsprp tb tu ekxlqae hh yijgbi stg yymvrk Lly
Ghss wvvq ess vsykgoid zt moi mmsi rlbzzxvv Qemmo moi Yyax.
"""


def get_count(text: str) -> int:
    count = 0
    for i in text:
        if i in ALPHABET:
            count += 1
    return count


def ioc(text: str) -> float:
    letterCounts = []

    # Loop through each letter in the alphabet - count number of times it appears
    for i in range(len(ALPHABET)):
        count = 0
        for j in text:
            if j == ALPHABET[i]:
                count += 1
        letterCounts.append(count)

    # Loop through all letter counts, applying the calculation (the sigma part)
    total = 0
    for i in range(len(letterCounts)):
        ni = letterCounts[i]
        total += ni * (ni - 1)

    n = get_count(text)
    total = float(total) / ((n * (n - 1)))
    return total


def main():
    ioc_val = ioc(EXAMPLE)
    print(f"IOC: {ioc_val}")


if __name__ == "__main__":
    main()
