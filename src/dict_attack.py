import fitness as f
import vigenere as vig
import re, string

PATTERN = re.compile('[\W_]+', re.UNICODE)

EXAMPLE = """
I kxjw mtmf eewcyj yurql yrd qwex. Mnf wurnags xb xxsaykl yc vgthaykm ur oxiqp wggemqxrhm
zgk m Ketdxjnw Tewvltdwnkaut chslccgg ur Phmsdnwk Egvxnfn ul mti Axw Pnrava Maltlcolx
aj Zbnlwa sgp Xrvhqxfgzk (RZM), UVJ zgk flr lpurhy, hr 2025. Ef t Pk.M. mlnpiam iq Lieigxrk
Sfryfvq, M nf edpyj ma gbgturvmmq ql tcdmyebo eaw rhbyskol fdioum lh eyciouc nzx pictrwvyfm
ilvee idllaqvvgg ph yvnoegboqjf sgp gnkeha agtxw. Garrdazhgx zr afjxwfug ptrhnl,
A amzr weynfgiqh fmrrwa sgmplmifjf, hkafyxm-vxfnbzk, ngd fxgenzmpttlxh kdupyl tkjn A
uqpvxvh fimep qnde pn uf xrjrvtley lxmgubnj xl jxeinkck jmkbexngt. Ph wgndwrpout cf Vdccmojauhak
eaw Asyfavmxvhnv, jfggs avmh ph ifzamaz rhbyskol vg Cuhjltzeyrslb ix Wukvmao
Fulxdqnkklwa, zte tehvlmyv fq avmh d bidbp jbnngjnahz ma uowq nzxavrmifjf sgp ecillnx
slbipms ro wgfbygxr vlcwgoi. Vg agmclbar, V tm fxhxbpiam iq vs suupvmy wx gsgmkr kevyiflufveiwryk
lggu ts dbmalfmaz iq cysvtmaz, gujxags, qrgtracfz exhweqcm, sgp gbeldkijtfmaz
oq aykxmvpa puxdwvfw. V tm fxgebfxrw tr jwswqqvv ealydeqrpx aqm qgnxh tkedcfq tbtexcljnw
mti bipranmguxl mo fxhlkufhme wx nzx hmokaqc uutpizbc fxgenzmgr aw cbw GYX.
Gaaqt sgn rse voqbcvxdmaz mb jjheugnmirw zgk flvl avbckmmrglhly. C dhao shrzjlv ma xux
prbmauupvmy ro xaloyfliqp bgp U gng crwnjbnygx tr cbw wqtnktpnhl’l ssnes. Wqufd ksh, liu.
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
