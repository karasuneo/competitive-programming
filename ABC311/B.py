N, D = map(int, input().split())

DAY = [["x"] * D] * N

ANS = 0
ANS_TMP = 0
CHECK = False


for i in range(N):
    DAY[i] = list(input())


for i in range(D):
    for j in range(N):
        if DAY[j][i] == "o":
            CHECK = True
        else:
            CHECK = False
            ANS_TMP = 0
            break
    if CHECK == True:
        ANS_TMP += 1
        if ANS_TMP > ANS:
            ANS += 1

print(ANS)
