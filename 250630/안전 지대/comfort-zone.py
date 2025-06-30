n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

k = 1
answer = (1, 0)

def dfs(x, y):
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if (new_x > -1 and new_x < n and new_y > -1 and new_y < m and visited[new_x][new_y] == 0 and grid[new_x][new_y] > k):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)


while (True):
    num = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if (visited[row][col] == 0 and grid[row][col] > k):
                visited[row][col] = 1
                num += 1
                dfs(row, col)
    if (num == 0):
        break

    if (num > answer[1]):
        answer = (k, num)
    k = k+1


print(answer[0], answer[1])
