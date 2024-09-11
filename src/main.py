import freq

AMBROSIA = """
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
AMBROSIA_PLAINTEXT = """
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


def main():
    map = freq.freq_map(AMBROSIA)
    freq.graph_freq_map(map)


if __name__ == "__main__":
    main()
