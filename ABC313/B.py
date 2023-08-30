# INPUT = input().split()
# N= int(INPUT[0])
# M=  int(INPUT[1])
# INFO = [[0 for i in range(2)] for j in range(M) ]

# for i in range(M):
#     INFO[i] = list(map(int, input().split()))
    


# print(INFO)

# 模範解答
N, M = map(int, input().split())
deg = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[b] += 1

ans = -1
for i in range(N):
    if deg[i] == 0:
        if ans != -1:
            print(-1)
            exit(0)
        else:
            ans = i + 1

print(ans)
