N = int(input())
S = input()

ANS = ["A", "B", "C"]

for i in range(N):
    for ans in ANS:
        if S[i] == ans:
            ANS.remove(ans)
    if len(ANS) == 0:
        print(i + 1)
        exit(0)
