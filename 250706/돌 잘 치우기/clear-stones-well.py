from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

start = []
for _ in range(k):
    xi, yi = map(int, input().split())
    start.append((xi-1, yi-1))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]

stone = []


def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def find_stone():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                stone.append((i, j))


def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < n and visited[x][y] == False and grid[x][y] == 0


cnt = 0


def bfs():
    global cnt
    while q:
        cur_loc = q.popleft()
        for i in range(4):
            new_x = cur_loc[0]+dx[i]
            new_y = cur_loc[1]+dy[i]
            if (can_go(new_x, new_y)):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
                cnt += 1


def cal_cnt():
    for i in range(len(start)):
        q.append((start[i][0], start[i][1]))
        bfs()


answer = 0


def find_max():
    global answer, cnt
    combi = list(combinations(stone, m))

    for poses in combi:
        for pos in poses:
            grid[pos[0]][pos[1]] = 0
        cnt = 0
        init_visited()
        cal_cnt()
        if cnt > answer:
            answer = cnt
        for pos in poses:
            grid[pos[0]][pos[1]] = 1


find_stone()
find_max()
print(answer)
