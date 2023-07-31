from typing import List
import json
from calc_ import Damage_Calc


filename = "./Preset/test.json"

MAIN = "メインステータス"
WD = "ウェポンダメージ"
CRIT = "クリティカル"
DH = "ダイレクトヒット"
DET = "意志力"
TNC = "不屈"
SD = "スキルの威力"
Sta_Lists = [MAIN, WD, CRIT, DH, DET, TNC, SD]


def Preset_y(read_data):
    num = 0
    print("どのプリセットを読み込みますか？")
    print(read_data)
    preset = int(input("数字で入力してください。"))
    length: int = len(read_data)
    while True:
        if preset < length:
            prest_name = f"pre{preset}"
            print("読み込みを完了しました")
            Main_sta = int(read_data[preset][prest_name][0])
            Wd_sta = int(read_data[preset][prest_name][1])
            Crit_sta = int(read_data[preset][prest_name][2])
            DH_sta = int(read_data[preset][prest_name][3])
            Det_sta = int(read_data[preset][prest_name][4])
            Tnc_sta = int(read_data[preset][prest_name][5])
            Trait = int(read_data[preset][prest_name][6])
            Attribute = int(read_data[preset][prest_name][7])
            instance = Damage_Calc(
                Main_sta,
                Wd_sta,
                Crit_sta,
                DH_sta,
                Det_sta,
                Tnc_sta,
                Attribute,
            )

            Atack_Rate = instance.Atack_Rate()

            WD_Damage = instance.WD_Damage()
            # 武器基本性能

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
            return [
                Atack_Rate,
                WD_Damage,
                Crit_Rate,
                Crit_Damage,
                DH_Rate,
                DET_Damage,
                TNC_Damage,
                Trait,
                Attribute,
            ]
        elif num == 4:
            raise ValueError("処理を終了。")
        else:
            print("入力が不正です。")
            num += 1
            print(read_data)
            preset = int(input("数字で入力してください。"))


def Status() -> List[int]:
    Main_sta: int = INPUT(MAIN)
    Wd_sta: int = INPUT(WD)
    Crit_sta: int = INPUT(CRIT)
    DH_sta: int = INPUT(DH)
    Det_sta: int = INPUT(DET)
    Tnc_sta: int = INPUT(TNC)
    # Skill__damage: int = INPUT(SD)
    return [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta]


# 入力時の処理
def INPUT(List) -> int:
    # 初期値
    num = 0
    print(f"{List}を入力してください")
    Status = input()
    if Status.isdecimal():
        return int(Status)
    # 数字じゃなかったら弾く
    else:
        while not Status or not Status.isdecimal():
            print(f"{List}が入力されていません。")
            print(f"{List}を入力してください")
            num += 1
            Status = input()
            # 4回入力なしだったら処理を終了する。
            if num == 4:
                raise ValueError("処理を終了")
        return int(Status)


def Roll_status() -> List[int]:
    num = 0
    print("近接ですか？キャスターですか？ヒーラーですか？ m/c/h で入力してください。")
    Roll = input()
    while True:
        # メレーの処理
        if Roll == "m":
            Trait: int = 100
            Attribute: int = 100
            break
        # キャスターの処理
        elif Roll == "c":
            Trait: int = 130
            Attribute: int = 100
            break
        # ヒーラーの処理
        elif Roll == "h":
            Trait: int = 130
            Attribute: int = 115
            break
        elif num == 4:
            raise ValueError("error")
        else:
            print("入力されいません。")
            print("近接ですか？キャスターですか？ヒーラーですか？ m/c/h で入力してください。")
            Roll = input()
            num += 1
    return [Trait, Attribute]


# プリセット保存
def Preset(Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Trait, Attribute):
    num = 0
    print("ステータスを保存しますか？ y/n")
    select = input()
    with open(filename, "r") as f:
        data = json.load(f)
        length = len(data)
        Preset_Name = f"pre{length}"
        while True:
            if select == "y":
                Save = {
                    Preset_Name: [
                        Main_sta,
                        Wd_sta,
                        Crit_sta,
                        DH_sta,
                        Det_sta,
                        Tnc_sta,
                        Trait,
                        Attribute,
                    ],
                }
                with open(filename, "r") as f:
                    read_data = json.load(f)
                if read_data == []:
                    with open(filename, "w") as f:
                        json.dump(Save, f)
                else:
                    with open(filename, "w") as f:
                        Data = [read_data, Save]
                        json.dump(Data, f)
                print("保存に成功しました。")
                return
            elif select == "n":
                print("保存がキャンセルされました。")
                return
            elif num == int(4):
                raise ValueError("処理を終了")
            else:
                print("入力が不正です。")
                num += 1
                select = input()


# 読み込み
def load():
    num = 0
    with open(filename, "r") as f:
        read_data = json.load(f)
        if read_data == []:
            [Trait, Attribute] = Roll_status()
            [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta] = Status()
            # Damage_calc インスタンス化
            instance = Damage_Calc(
                Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Attribute
            )
            Preset(
                Main_sta,
                Wd_sta,
                Crit_sta,
                DH_sta,
                Det_sta,
                Tnc_sta,
                Trait,
                Attribute,
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
            return [
                Atack_Rate,
                WD_Damage,
                Crit_Rate,
                Crit_Damage,
                DH_Rate,
                DET_Damage,
                TNC_Damage,
                Trait,
                Attribute,
            ]
        else:
            print("プリセットを読み込みますか？ y/n")
            Select = input()
            while True:
                if Select == "y":
                    return Preset_y(read_data)
                elif Select == "n":
                    [Trait, Attribute] = Roll_status()
                    [Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta] = Status()
                    # Damage_calc インスタンス化
                    instance = Damage_Calc(
                        Main_sta, Wd_sta, Crit_sta, DH_sta, Det_sta, Tnc_sta, Attribute
                    )
                    Preset(
                        Main_sta,
                        Wd_sta,
                        Crit_sta,
                        DH_sta,
                        Det_sta,
                        Tnc_sta,
                        Trait,
                        Attribute,
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
                    return [
                        Atack_Rate,
                        WD_Damage,
                        Crit_Rate,
                        Crit_Damage,
                        DH_Rate,
                        DET_Damage,
                        TNC_Damage,
                        Trait,
                        Attribute,
                    ]
                elif num == 4:
                    raise ValueError("処理を終了")
                else:
                    print("入力が不正です。")
                    num += 1
                    Select = input()
