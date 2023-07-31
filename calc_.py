from decimal import Decimal
import math
import random


class Damage_Calc:
    def __init__(
        self,
        Main_Status: int,
        WP_Damage: int,
        CRIT: int,
        DH: int,
        DET: int,
        TNC: int,
        Attribute: int,
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
        self.Attribute: int = int(Attribute)
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

    def WD_Damage(self):
        Result = Decimal(
            (self.default["LvMain"] * self.Attribute / 1000) + self.WP_Damage
        )
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
class Skill_Damage:
    def __init__(
        self, Potency: int, Trait: int, Attribute, ATK: int, DET: int, WD: int, TNC: int
    ) -> None:
        self.Potency: int = int(Potency)
        self.Trait: int = int(Trait)
        self.Attribute: int = int(Attribute)
        self.ATK: int = int(ATK)
        self.DET: int = int(DET)
        self.WD: int = int(WD)
        self.TNC: int = int(TNC)

    def D1(
        self,
    ) -> int:
        D1_Result: int = Decimal(self.Potency * self.ATK * self.DET / 100 / 1000)
        D1_Final_Result: int = math.floor(D1_Result)
        return D1_Final_Result

    def D2(self, D1) -> int:
        Result = Decimal(D1 * self.TNC / 1000 * self.WD / 100 * self.Trait / 100)
        D2_Final_Result: int = math.floor(Result)
        return D2_Final_Result

    def D2_Random(self, D2: int) -> int:
        Value: int = D2
        low = Value * 0.9
        up = Value * 1.1
        Result = Decimal(random.uniform(low, up))
        Final_Result: int = math.floor(Result)
        return Final_Result
