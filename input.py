def INPUT(List) -> int:
    num = 0
    print(f"{List}を入力してください")
    Status = input()
    while not Status:
        print(f"{List}が入力されていません。")
        print(f"{List}を入力してください")
        num += 1
        Status = input()
        if num == 5:
            raise ValueError("処理を終了")
    return Status
