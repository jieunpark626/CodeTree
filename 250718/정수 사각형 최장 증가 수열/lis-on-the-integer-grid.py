from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
max_loc = (-1, -1)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]

def init():
    global dp, visited
    for r in range(n):
        for c in range(n):
            visited[r][c] = False
            dp[r][c] = 0

def Print(arr):
    for r in arr:
        print(r)
    print()


def find_max_loc(arr):
    global max_loc
    max_val = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] > max_val:
                max_val = arr[r][c]
                max_loc = (r, c)


def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

answer = 0
dp[0][0] = 1
for cx in range(0, n):
    for cy in range(0, n):
        for i in range(4):
            if(dp[cx][cy] == 0):
                dp[cx][cx] = 1
            nx, ny = cx + dx[i], cy+dy[i]
            if (can_go(nx, ny) and grid[nx][ny] > grid[cx][cy]):
                dp[nx][ny] = max(dp[cx][cy]+1, dp[nx][ny])


find_max_loc(dp)                
print(dp[max_loc[0]][max_loc[1]])