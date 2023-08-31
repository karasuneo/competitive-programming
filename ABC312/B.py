N, M = map(int, input().split())
GRID = [["." for i in range(M)] for j in range(N)]


for i in range(N):
    grid = list(input())
    GRID[i] = grid


for y in range(N - 3):
    for x in range(M - 3):
        if GRID[x][y] == "#":
            if (
                GRID[x + 1][y] == "#"
                and GRID[x + 2][y] == "#"
                and GRID[x][y + 1] == "#"
                and GRID[x][y + 2] == "#"
                and GRID[x + 1][y + 1] == "#"
                and GRID[x + 2][y + 2] == "#"
            ):
                print(x + 1, y + 1)
