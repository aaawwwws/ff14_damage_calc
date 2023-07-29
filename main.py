from typing import List, Dict
from calc import Skill_Damage
from input import Skill_damage


def Main_func():
    try:
        insntace = Skill_Damage(Skill_damage, 130)
        D1 = insntace.D1()
        D2 = insntace.D2(D1, 130)
        print(D2)

    except ValueError as e:
        print(e)


Main_func()
