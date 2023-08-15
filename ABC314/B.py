data_list = []
ans_data_list = []

# 人数
N = int(input())


for i in range(N):
    # かける目の数
    C = int(input())
    # かける目
    A = [int(tok) for tok in input().split()]

    data_list.append({"index": i + 1, "num": C, "bet": A})

# かけた番号
X = int(input())


# print(data_list)

# 入力をもとに作成した辞書型の配列を操作して、betにXが含まれている辞書型を探す
for index, dl in enumerate(data_list):
    for bet in dl["bet"]:
        if X == bet:
            ans_data_list.append(dl)

# 該当する数値がない場合は0を返す
if ans_data_list == []:
    print(0)
else:
    # 最も小さい num の値を取得
    min_num = min(entry["num"] for entry in ans_data_list)

    # num が最小の辞書型の index を取得
    min_num_indices = [
        entry["index"] for entry in ans_data_list if entry["num"] == min_num
    ]

    print(len(min_num_indices))
    # 空白区切りで index を出力
    print(*min_num_indices)
