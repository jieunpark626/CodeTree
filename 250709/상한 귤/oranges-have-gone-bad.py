from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
rotten = []
init_rotten = []
answer = [[0 for _ in range(n)] for _ in range(n)]


def init_answer():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                answer[i][j] = -1
            if grid[i][j] == 2:  # 최초 상한 귤
                init_rotten.append((i, j))
                rotten.append((i, j))


def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < n and visited[x][y] == False and grid[x][y] == 1 and answer[x][y] == 0


def bfs():
    while q:
        cur_loc = q.popleft()

        for i in range(4):
            new_x = cur_loc[0] + dx[i]
            new_y = cur_loc[1] + dy[i]

            if (can_go(new_x, new_y)):
                answer[new_x][new_y] = answer[cur_loc[0]][cur_loc[1]] + 1
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
                rotten.append((new_x, new_y))


init_answer()

while (True):
    cnt = len(rotten)
    for loc in rotten:
        q.append(loc)
    bfs()
    if (cnt == len(rotten)):
        break

for i in range(n):
    for j in range(n):
        if (answer[i][j] == 0 and (i,j) not in init_rotten):
            answer[i][j] = -2

for row in answer:
    for i in row:
        print(i, end = " ")
    print()