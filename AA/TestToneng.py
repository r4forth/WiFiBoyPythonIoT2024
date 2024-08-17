import machine
from lib.toneng import toneng
# 音階符號 : CDEFGAB   (Do Re Mi Fa So La Si)
# o + 數字 : o4 代表選擇移動到鋼琴第四組八度音階，O3 就是第三組八度音階。
# >        : 升一個八度音階
# <        : 降一個八度音階
# #        : 加在音階符號後面，代表升半音
# b        : 加在音階符號後面，代表降半音
# 數字     : 1, 2, 4, 8, 16, 32等數字就是「幾分音符」的意思。


toneng.tempo(75)
# 歌曲
psA = "CDECCDECEFG.EFG.E.G2A.G2DECG2A.G2DECCGC.CGC."
ps0 = 'CDEFGAB'
ps1 = "CC#DD#EFF#GG#AA#B"
ps2 = "CEFG1CEFG1CEFG2E2C2E2D1EEDC1CE2G2GF1EFG2E2C2D2C1"
ps3 = "GEE2FDD2CDEFGGG2GEE2FDD2CEGGC1DDDDDEF2EEEEEFG2GEE2FDD2CEGGC1"
ps4 = "O3CDECCDECEFG2EFG2G8A8G8F8ECG8A8G8F8ECDO2GO3C2DO2GO3C2"
ps5 = "C8C#8D8D#8E8F8F#8G8G#8A8A#8B8"
ps6 = "O3E1D1C1O2B1A1G1A1B1O3C1O2B1A1G1F1E1F1D1O3CO2BO3CO2CO1BO2GDECO3CO2BABO3EGAFEDFEDCO2BAGFEDFED" #Canon1
ps7="CDEFGDGFEAGFGFEDCO1AO2ABO3CO2BAGFEDAGAGFE2O3E2D1C1D1C2E2D2F2" #Canon2
ps8="O4DO3BGO4DO3BGO4DO3BGO4DECO3GO4ECO3GO4EDO3BGO4DO3BGO4DO3BGADAO4DFA"
ps9="G>C<BGCC2GDDEFEE2.G>C<BCC2GDDEFEE2.G>DC<B>CC2DEECC2<A2B>CC<GG2GFEDDCCDD1.." # 告白氣球
ps10=".8C8C8<B8>C.8<B8>C8<B>C.D.8<B8B8A8B.8A8B8A8B.>C.2<A>CEDCE1.1."

toneng.play(psA)
# while True:
#     if wb.getkey() == 1:
#         toneng.play(ps1)
#     if wb.getkey() == 2:
#         toneng.play(ps2)
#     if wb.getkey() == 3:
#         toneng.play(ps3)
#     if wb.getkey() == 4:
#         toneng.play(ps4)
#     if wb.getkey() == 5:
#         toneng.play(ps5)    
#     if wb.getkey() == 6:
#         toneng.play(ps6)    
#     if wb.getkey() == 7:
#         toneng.play(ps7)
#     if wb.getkey() == 8:
#         toneng.play(ps8)
#     if wb.getkey() == 9:
#         toneng.play(ps9)
#     if wb.getkey() == 10:
#         toneng.play(ps10)
#     if wb.getkey() == 32:
#         break
#     if wb.getkey() == 64:
#         break