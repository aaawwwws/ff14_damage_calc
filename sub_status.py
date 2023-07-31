from input_ import INPUT
from typing import List

MAIN = "メインステータス"
WD = "ウェポンダメージ"
CRIT = "クリティカル"
DH = "ダイレクトヒット"
DET = "意志力"
TNC = "不屈"
SD = "スキルの威力"
Sta_Lists = [MAIN, WD, CRIT, DH, DET, TNC, SD]


def Status() -> List[int]:
    Main_sta: int = INPUT(MAIN)
    Wd_sta: int = INPUT(WD)
    Crit_sta: int = INPUT(CRIT)
    DH_sta: int = INPUT(DH)
    Det_sta: int = INPUT(DET)
    Tnc_sta: int = INPUT(TNC)
    Skill__damage: int = INPUT(SD)
    return [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Skill__damage]
