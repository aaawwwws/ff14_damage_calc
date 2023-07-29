from decimal import Decimal
from typing import List, Dict
from sub_status import main, WD, CRIT, DH, DET, TNC, Sta_Lists
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


MAIN: int = INPUT(main)
WD: int = INPUT(WD)
CRIT: int = INPUT(CRIT)
DH: int = INPUT(DH)
DET: int = INPUT(DET)
TNC: int = INPUT(TNC)


def Main_func():
    const = Damage_Calc(MAIN, WD, CRIT, DH, DET, TNC)
    try:
        print(
            f"クリティカル発生率{const.Crit_Rate()}%,クリティカル倍率{ const.Crit_Damage()}%ダイレクトヒット発生率{const.DH_Damage()}%"
        )
    except ValueError as e:
        print(e)


Main_func()
