# INPUT = input().split()
# N= int(INPUT[0])
# M=  int(INPUT[1])
# INFO = [[0 for i in range(2)] for j in range(M) ]

# for i in range(M):
#     INFO[i] = list(map(int, input().split()))


# print(INFO)

# 模範解答
#  TODO:肝はグラフ理論で学んだそれぞれのノードに幾つの矢印が伸びているかの「次数」の数
# N, Mをスペースで区切って入力し、整数として取得
N, M = map(int, input().split())

# 頂点ごとの次数を格納するリストを初期化
deg = [0] * N
print(deg)

# 辺の情報を入力して処理
for _ in range(M):
    # input().split()ないの要素を全てint型に変換し、abに格納
    a, b = map(int, input().split())
    # 配列の処理をやりやすくするため-1をしている
    a -= 1
    b -= 1
    deg[b] += 1


# ansを初期化（後で答えを格納）
ans = -1

# 各頂点の次数を調べるループ
for i in range(N):
    # もし次数が0ならば
    if deg[i] == 0:
        # すでに答えが見つかっていた場合
        if ans != -1:
            print(-1)  # 答えが複数あるので -1 を出力
            exit(0)  # プログラム終了
        else:
            ans = i + 1  # 答えを記録

# 最終的な答えを出力
print(ans)

