N, P, Q = map(int, input().split())


GOODS = list(map(int, input().split()))


if (Q + min(GOODS)) > P:
    print(P)
else:
    print(Q + min(GOODS))
