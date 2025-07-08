from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 뱀 : 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[False for _ in range(m)] for _ in range(n)]
route = [[0 for _ in range(m)] for _ in range(n)]

q = deque()


def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < m and grid[x][y] != 0 and visited[x][y] == False


answer = 0


def bfs():
    while q:
        cur_loc = q.popleft()

        if (cur_loc[0] == n-1 and cur_loc[1] == m-1):
            print(route[cur_loc[0]][cur_loc[1]])
            return
        for i in range(3):
            new_x = cur_loc[0] + dx[i]
            new_y = cur_loc[1] + dy[i]

            if (can_go(new_x, new_y)):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
                route[new_x][new_y] = route[cur_loc[0]][cur_loc[1]] + 1
    print(-1)
q.append((0,0))
bfs()