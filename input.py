from sub_status import MAIN, WD, CRIT, DH, DET, TNC, Sta_Lists, SD


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


Main_sta: int = INPUT(MAIN)
Wd_sta: int = INPUT(WD)
Crit_sta: int = INPUT(CRIT)
DH_sta: int = INPUT(DH)
Det_sta: int = INPUT(DET)
Tnc_sta: int = INPUT(TNC)
Skill_damage: int = INPUT(SD)
