from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

sx -= 1
sy -= 1
ex -= 1
ey -= 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()

walls = []
remove_walls = []
visited = [[False for _ in range(n)] for _ in range(n)]
route = [[0 for _ in range(n)] for _ in range(n)]
min_time = 10000

# n


def get_walls():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                walls.append((i, j))


def init():
    q.append((sx, sy))
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            route[i][j] = 0


comb_result = []


def combinations(idx):
    global remove_walls
    if (len(comb_result) == k):
        tmp = comb_result.copy()
        remove_walls.append(tmp)
    for i in range(idx, len(walls)):
        comb_result.append(walls[i])
        combinations(i+1)
        comb_result.pop()


def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 0 and visited[x][y] == False


def bfs():
    while q:
        cur_loc = q.popleft()
        if (cur_loc[0] == ex and cur_loc[1] == ey):
            return route[cur_loc[0]][cur_loc[1]]
        for i in range(4):
            newx, newy = cur_loc[0]+dx[i], cur_loc[1]+dy[i]
            if (can_go(newx, newy)):
                visited[newx][newy] = True
                route[newx][newy] = route[cur_loc[0]][cur_loc[1]] + 1
                q.append((newx, newy))
    return -1


def remove(arr):
    for i in range(k):
        x, y = arr[i][0], arr[i][1]
        grid[x][y] = 0


get_walls()
combinations(0)
for combi in remove_walls:
    # remove
    for i in range(k):
        x, y = combi[i][0], combi[i][1]
        grid[x][y] = 0
    init()
    time = int(bfs())
    if (time != -1 and time < min_time):
        min_time = time
    # init
    for i in range(k):
        x, y = combi[i][0], combi[i][1]
        grid[x][y] = 1

if(min_time == 10000):
    print(-1)
else:
    print(min_time)
