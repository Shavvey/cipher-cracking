import fitness as f
import vigenere as vig


EXAMPLE = """
ucicjua, ksblnq, yfcgxgjmcj, cmgh bp ymqi mtvh; t cmiv bh fjcy awvatv, czt rk gztmhp hgi. kpx iktl rdrb fic oo jemml eueep pymf; xwp gmku ql sue ilpvzkis hird kpxmg molaj; ah pte ir xv ebxw nacorz. mlt yozhv jkyifs
fwkp msao ymq tixwpc wyo ruumitoso: zn bx lprc of, qm apd a enzmosjd fyqcb, trs rrgamwnwaj hypy ktihlr yjjexv’s tt. faim, nrspr jardx su mrspla trs ehc nvam–jdc bpqkcl mh ln fkewnvpmlc irv; ls pce rdvg tpa, llj dfvhyglbja dmg– gdxe g pf aiipv il yrmleg’d fsjvztp. wp wyo dg yvxpnb, brqmlufl yju rnwi eo ka: scm fgftso jirw wp wyo ruumitoso; rvw fgftso za tr wznmqiiupt xal. dv ptxw mrmqxpm qpyy awgbbztd hmiv bh vdxe
udfax vpysmij lbh ise eaemkea nodbvzl jxwl: beu bamh tn awvatv hpek wdjbxxzuq? symg xwlt rdv xhsg sata tzbis, nacorz aeis wclk:
iffxeimj jphyao bc irlx su dtcnemk wiffd: uvb uvjeuq orgl lt haq wdjbxxzuq; wel uvjeuq ej ig ldyosnrjei bln. wkl iep std qav baei zn rdv tnttccyh z bavxne nnvaxripd fed i dmcrlw yiwpr, lsiad ym wms ehpetm kiufsc: sra mlxd akxzbbsc?
jer xicmyh dawo ym peh lmzekqhyh; lnb, olzx, lt ts yj ywgsjcazhv utr. x dpcwb vhx iz dgogzhzt hhyp sznxjd snkbm, uyi sepa z if xd dpcwb eaei t dm gewp. cdf ajh uqw pdge fed wggt, yor szbasje cyqjm: plpe cyqjm pmishmhua rsj ehcj, kw fsjcn dki pbq?
d uubcdmgx! isos wib ypto tm xicmmhs bcwjbl, eco mcj yioi azsr pymbv gpaqke. jxeg hird dm; fc wpapp za br ise akwnbr isepa nqml rleqwi,
igh x xuqp ginwt eijh zb vsbp byyb bh qt.
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
