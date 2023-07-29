from decimal import Decimal


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

    def TNC_Damage(self) -> float:
        Result = Decimal(
            110 * (self.TNC - self.default["LvSub"]) / self.default["LvDiv"] + 1000
        )
        Result_floor = round(Result, 0)
        return Result_floor
