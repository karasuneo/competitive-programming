N, H, X = map(int, input().split())

ME = [int(x) for x in input().split()]

ANS = ME.index(max(ME)) + 1

for index, me in enumerate(ME):
    if (H + me) >= X and ME[ANS - 1] > me:
        ANS = index + 1

print(ANS)
