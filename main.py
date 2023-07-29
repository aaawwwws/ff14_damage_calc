from decimal import Decimal
from typing import List, Dict
from sub_status import MAIN, WD, CRIT, DH, DET, TNC, Sta_Lists
from input import INPUT


class Damage_Calc:
    def __init__(
        self, Main_Status: int, WP_Damage: int, CRIT: int, DH: int, DET: int, TNC: int
    ) -> None:
        # メインステータス(STR)とかの値を取る
        self.Main_Status: int = int(Main_Status)
        # ウェポンダメージ
        self.WP_Damage: int = int(WP_Damage)
        # サブステの値を取る
        self.CRIT: int = int(CRIT)
        self.DH: int = int(DH)
        self.DET: int = int(DET)
        self.TNC: int = int(TNC)
        self.default: dict[str, int] = {
            "LvMain": int(390),
            "LvSub": int(400),
            "LvDiv": int(1900),
        }

        # クリティカル発生率

    def Crit_Rate(self) -> float:
        Result = Decimal(
            (200 * (self.CRIT - self.default["LvSub"]) / self.default["LvDiv"] + 50)
            / 10
        )

        Result_floor = round(Result, 1)
        return Result_floor

        # クリティカルダメージ

    def Crit_Damage(self) -> float:
        Result = Decimal(
            (200 * (self.CRIT - self.default["LvSub"]) / self.default["LvDiv"] + 1400)
            / 10
        )
        Result_floor = round(Result, 1)
        return Result_floor

        # ダイレクトヒットダメージ

    def DH_Damage(self) -> float:
        Result = Decimal(
            550 * (self.DH - self.default["LvSub"]) / self.default["LvDiv"] / 10
        )
        Result_floor = round(Result, 1)
        return Result_floor


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
            f"クリティカル発生率{const.Crit_Rate()}%,クリティカル倍率{ const.Crit_Damage()}%ダイレクトヒット発生率{const.DH_Damage()}%"
        )
    except ValueError as e:
        print(e)


Main_func()
