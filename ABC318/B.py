# N = int(input())
# INPUT = []

# for i in range(N):
#     arr = [int(x) for x in input().split()]
#     INPUT.append(arr)

# for input in INPUT:
#     area = (input[1] - input[0]) * (input[3] - input[2])
#     # print(area)


# for i, one_input in enumerate(INPUT):
#     i_area = (one_input[1] - one_input[0]) * (one_input[3] - one_input[2])
#     for j, two_input in enumerate(INPUT):
#         if j != i:
#             if one_input[0] <= two_input[0]
#             j_area = (two_input[1] - two_input[0]) * (two_input[3] - two_input[2])

N = int(input())
g = [[False for i in range(100)] for i in range(100)]
for k in range(N):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            g[i][j] = True
ans = 0
for i in range(100):
    for j in range(100):
        if g[i][j] == True:
            ans += 1
print(ans)
