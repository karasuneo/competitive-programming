N, M = map(int, input().split())

GOODS = [[] for i in range(N)]
JUDGE = False

for i in range(N):
    GOODS[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i != j and (
            (GOODS[i][0] == GOODS[j][0] and len(GOODS[i]) > len(GOODS[j]))
            or (GOODS[i][0] < GOODS[j][0] and len(GOODS[i]) >= len(GOODS[j]))
        ):
            good_i = GOODS[i][2:]
            good_j = GOODS[j][2:]

            if list(set(good_i) & set(good_j)) == good_j:
                print("Yes")
                exit(0)

print("No")
