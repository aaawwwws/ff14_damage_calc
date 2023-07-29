# 入力時の処理
def INPUT(List) -> int:
    # 初期値
    num = 0
    print(f"{List}を入力してください")
    Status = input()
    if Status.isdecimal():
        return Status
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
        return Status
