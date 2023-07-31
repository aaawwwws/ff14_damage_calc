from typing import List
from input_ import Roll_status, INPUT
from calc_ import Damage_Calc, Skill_Damage
from sub_status import Status, SD


def main():
    [Trait, Attribute] = Roll_status()
    [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta] = Status()
    # Damage_calc インスタンス化
    instance = Damage_Calc(
        Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Attribute
    )

    # 攻撃魔法威力
    Atack_Rate = instance.Atack_Rate()

    # 武器基本性能
    WD_Damage = instance.WD_Damage()

    # クリティカル発生率
    Crit_Rate = instance.Crit_Rate()

    # クリティカルダメージ
    Crit_Damage = instance.Crit_Damage()

    # ダイレクトヒット
    DH_Rate = instance.DH_Rate()

    # 意志力ダメージ
    DET_Damage = instance.DET_Damage()

    # 不屈ダメージ
    TNC_Damage = instance.TNC_Damage()

    # D2インスタンス化
    skill_damage = Skill_Damage(
        INPUT(SD), Trait, Attribute, Atack_Rate, DET_Damage, WD_Damage, TNC_Damage
    )
    D1 = skill_damage.D1()
    print(skill_damage.D2(D1))


main()
