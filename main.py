from typing import List
from input_ import INPUT, load
from calc_ import Skill_Damage
from sub_status import SD


def main():
    [
        Atack_Rate,
        WD_Damage,
        Crit_Rate,
        Crit_Damage,
        DH_Rate,
        DET_Damage,
        TNC_Damage,
        Trait,
        Attribute,
    ] = load()

    # D2インスタンス化
    skill_damage = Skill_Damage(
        INPUT(SD), Trait, Attribute, Atack_Rate, DET_Damage, WD_Damage, TNC_Damage
    )

    D1 = skill_damage.D1()
    D2: int = skill_damage.D2(D1)
    print(D2)

    for i in range(10):
        D2_random = skill_damage.D2_Random(D2)
        print(i, D2_random)
    input("press close to exit")


main()
