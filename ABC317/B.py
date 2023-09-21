N = int(input())

A = [int(x) for x in input().split()]


for a1 in A:
    CHECK = False
    for a2 in A:
        if a1 + 1 == a2:
            CHECK = True
            break

    if a1 != max(A) and CHECK == False:
        print(a1 + 1)
        break
