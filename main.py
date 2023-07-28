from decimal import Decimal
from typing import List, Dict
import math

from sqlalchemy import null

[Main, WD, CRIT, DH, DET, TNC] = [
    "メインステータス",
    "ウェポンダメージ",
    "クリティカル",
    "ダイレクトヒット",
    "意志力",
    "不屈",
]


def INPUT(List):
    print(f"{List}を入力してください")
    Status = input()
    if not Status:
        print("入力されていません。")
        return input()
    else:
        return Status


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

    def Crit_Rate(self):
        Result = Decimal(
            (200 * (self.CRIT - self.default["LvSub"]) / self.default["LvDiv"] + 50)
            / 10
        )

        Result_floor = round(Result, 1)
        return Result_floor

        # クリティカルダメージ

    def Crit_Damage(self):
        Result = Decimal(
            (200 * (self.CRIT - self.default["LvSub"]) / self.default["LvDiv"] + 1400)
            / 10
        )
        Result_floor = round(Result, 1)
        return Result_floor

        # ダイレクトヒットダメージ

    def DH_Damage(self):
        Result = Decimal(
            550 * (self.DH - self.default["LvSub"]) / self.default["LvDiv"] / 10
        )
        Result_floor = round(Result, 1)
        return Result_floor


const = Damage_Calc(
    INPUT(Main), INPUT(WD), INPUT(CRIT), INPUT(DH), INPUT(DET), INPUT(TNC)
)


def Main():
    print(
        f"クリティカル発生率{const.Crit_Rate()}%,クリティカル倍率{ const.Crit_Damage()}%ダイレクトヒット発生率{const.DH_Damage()}%"
    )
