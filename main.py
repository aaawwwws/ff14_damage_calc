from typing import List
from input_ import Roll_status
from calc_ import Damage_Calc
from sub_status import Status


def main():
    [Trait, Attribute] = Roll_status()
    [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Skill__damage] = Status()
    instance = Damage_Calc(
        Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Skill__damage, Attribute
    )


main()
