N, M, P = map(int, input().split())
ANS = 0
CHECK_MOON = P

for i in range(1, N + 1):
    if i == M:
        ANS += 1
    if i == M + CHECK_MOON:
        CHECK_MOON += P
        ANS += 1

print(ANS)
