from typing import List, Dict
from sub_status import MAIN, WD, CRIT, DH, DET, TNC, Sta_Lists
from input import INPUT
from calc import Damage_Calc


Main_sta: int = INPUT(MAIN)
Wd_sta: int = INPUT(WD)
Crit_sta: int = INPUT(CRIT)
DH_sta: int = INPUT(DH)
Det_sta: int = INPUT(DET)
Tnc_sta: int = INPUT(TNC)


def Main_func():
    const = Damage_Calc(Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta)
    try:
        print(
            f"クリティカル発生率{const.Crit_Rate()}%,クリティカル倍率{ const.Crit_Damage()}%ダイレクトヒット発生率{const.DH_Rate()}%意志力倍率{const.DET_Damage()}不屈倍率{const.TNC_Damage()}"
        )
    except ValueError as e:
        print(e)


Main_func()
