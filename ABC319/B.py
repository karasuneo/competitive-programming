N = int(input())
ANS = []

for i in range(N + 1):
    CHECK = False
    for j in range(1, 10):
        if i == 0:
            ANS.append(str(1))
            CHECK = True
            break

        quotient = N / j
        if i != 0 and (N % j) == 0 and (i % quotient) == 0:
            ANS.append(str(j))
            CHECK = True
            break
    if CHECK == False:
        ANS.append("-")

print("".join(map(str, ANS)))
