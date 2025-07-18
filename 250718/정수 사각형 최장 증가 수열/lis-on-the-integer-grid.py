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
    return x >= 0 and x < n and y >= 0 and y < n and visited[x][y] == False


def bfs():
    while (q):
        cur_loc = q.popleft()
        cx, cy = cur_loc[0], cur_loc[1]
        for i in range(4):
            nx, ny = cx + dx[i], cy+dy[i]
            if (can_go(nx, ny) and grid[nx][ny] < grid[cx][cy] and dp[nx][ny]<dp[cx][cy]+1):
                visited[nx][ny] = True
                dp[nx][ny] = dp[cx][cy]+1
                q.append((nx, ny))
answer = 0
for r in range(n):
    for c in range(n):
        init()
        q.append((r, c))
        dp[r][c] = 1
        visited[r][c] = True
        bfs()
        find_max_loc(dp)
        
        if(dp[max_loc[0]][max_loc[1]] > answer):
            answer = dp[max_loc[0]][max_loc[1]]
            
print(answer)