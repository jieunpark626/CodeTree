import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]

zone_num = 0


def dfs(x, y, k):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (new_x > -1 and new_x < n and new_y > -1 and new_y < m and visited[new_x][new_y] == False and grid[new_x][new_y] > k):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)


def get_zone_num(k):
    global zone_num
    zone_num = 0

    for i in range(n):
        for j in range(m):
            visited[i][j] = False

    for row in range(n):
        for col in range(m):
            if (visited[row][col] == False and grid[row][col] > k):
                visited[row][col] = True
                zone_num += 1
                dfs(row, col, k)


max_zone_num = -1
answer_k = 0
max_height = 100
for k in range(1, max_height+1):
    get_zone_num(k)
    if (zone_num > max_zone_num):
        max_zone_num, answer_k = zone_num, k
print(answer_k, max_zone_num)
