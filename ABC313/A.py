# N = int(input())
# P = []
# MAX = 0
# x = 0

# P = [int(p) for p in input().split()]

# for i in range(len(P)):
#     if MAX < P[i]:
#         MAX = P[i]

# if P[0] == MAX:
#     count = 0
#     for p in P:
#         if p == MAX:
#             count += 1
#     if count > 1:
#         x = MAX - P[0] + 1
#         print(x)
#     else:
#         print(0)
# else:
#     x = MAX - P[0] + 1
#     print(x)


# 模範解答
n = int(input())
p = list(map(int, input().split()))
m = 0

for i in range(1, n):
    m = max(m, p[i])
print(max(0, m + 1 - p[0]))
