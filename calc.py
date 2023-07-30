from decimal import Decimal
from input import Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta
import math


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

        # 攻撃魔法威力

    def Atack_Rate(self) -> int:
        Result = Decimal(
            195 * (self.Main_Status - self.default["LvMain"]) / self.default["LvMain"]
            + 100
        )
        return Result

        # 武器基本性能

    def WD_Damage(self, Attribute):
        Result = Decimal((self.default["LvMain"] * Attribute / 1000) + self.WP_Damage)
        F_Result = math.floor(Result)
        return F_Result
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

        # ダイレクトヒット確率

    def DH_Rate(self) -> float:
        Result = Decimal(
            550 * (self.DH - self.default["LvSub"]) / self.default["LvDiv"] / 10
        )
        Result_floor = round(Result, 1)
        return Result_floor

        # 意志力ダメージ

    def DET_Damage(self) -> float:
        Result = Decimal(
            140 * (self.DET - self.default["LvMain"]) / self.default["LvDiv"] + 1000
        )
        Result_floor = round(Result, 0)
        return Result_floor

        # 不屈

    def TNC_Damage(self) -> float:
        Result = Decimal(
            110 * (self.TNC - self.default["LvSub"]) / self.default["LvDiv"] + 1000
        )
        Result_floor = round(Result, 0)
        return Result_floor


# さらちゃんブログの式を参照してください
class Skill_Damage(Damage_Calc):
    def __init__(self, Potency: int, Trait: int, Attribute) -> None:
        self.Potency: int = Potency
        self.Status = Damage_Calc(Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta)
        self.ATK: int = int(self.Status.Atack_Rate())
        self.DET: int = int(self.Status.DET_Damage())
        self.WD: int = int(self.Status.WD_Damage(Attribute))
        self.TNC: int = int(self.Status.TNC_Damage())
        self.Trait: int = int(Trait)

    def D1(self) -> int:
        D1_Result: int = Decimal(self.Potency * self.ATK * self.DET / 100 / 1000)
        D1_Final_Result: int = math.floor(D1_Result)
        return D1_Final_Result

    def D2(self, D1: int) -> int:
        Result = Decimal(D1 * self.TNC / 1000 * self.WD / 100 * self.Trait / 100)
        D2_Final_Result: int = math.floor(Result)
        return D2_Final_Result
