from typing import List, Dict
from calc import Skill_Damage
from input import Skill_damage


class Input:
    @staticmethod
    def Roll():
        num = 0
        try:
            print("近接ですか？キャスターですか？ヒーラーですか？ m/c/h で入力してください。")
            Roll_bool = input()
            while True:
                if Roll_bool == "m":
                    insntace = Skill_Damage(Skill_damage, 100, 100)
                    break
                if Roll_bool == "c":
                    insntace = Skill_Damage(Skill_damage, 130, 100)
                    break
                if Roll_bool == "h":
                    insntace = Skill_Damage(Skill_damage, 130, 115)
                    break
                if num == 4:
                    raise ValueError("error")
                else:
                    print("入力されいません。")
                    print("近接ですか？キャスターですか？ヒーラーですか？ m/c/h で入力してください。")
                    Roll_bool = input()
                    num += 1

            D1 = int(insntace.D1())
            D2 = insntace.D2(D1)
            print(D2)
        except ValueError as e:
            print(e)


Input.Roll()
