from typing import List


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
        if Roll == "c":
            Trait: int = 130
            Attribute: int = 100
            break
        # ヒーラーの処理
        if Roll == "h":
            Trait: int = 130
            Attribute: int = 115
            break
        if num == 4:
            raise ValueError("error")
        else:
            print("入力されいません。")
            print("近接ですか？キャスターですか？ヒーラーですか？ m/c/h で入力してください。")
            Roll = input()
            num += 1
    return [Trait, Attribute]
