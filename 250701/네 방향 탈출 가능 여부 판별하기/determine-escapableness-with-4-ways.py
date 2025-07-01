n, m = map(int, input().split())
grid = [list(map(int, input().split()))
        for _ in range(n)]  # 뱀:0, 없음:1, 도착점:(n-1,m-1)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = []
q.append((0, 0))

visited = [[False for _ in range(m)] for _ in range(n)]

def can_go(x, y):
    return x >= 0 and x < n and y >= 0 and y < m and visited[x][y] == False and grid[x][y] == 1


def bfs():
    while q:
        cur_loc = q.pop()
        if(cur_loc == (n-1,m-1)):
            return 1
        for i in range(4):
            new_x, new_y = cur_loc[0]+dx[i], cur_loc[1]+dy[i]
            if(can_go(new_x,new_y)):
                visited[new_x][new_y] = True
                q.append((new_x,new_y))
    return 0

print(bfs())
