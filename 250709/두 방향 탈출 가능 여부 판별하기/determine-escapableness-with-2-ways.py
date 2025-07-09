from collections import deque

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1]
dy = [1,0]

visited = [[False for _ in range(m)] for _ in range(n)]

def can_go(x,y):
    return x>=0 and x<n and y>=0 and y<m and visited[x][y] == False and grid[x][y] == 1

# flag = 0
# def dfs(x,y):
#     global flag
#     if(x == n-1 and y == m-1):
#         flag = 1
#         print(1)
#         return
#     for i in range(2):
#         new_x = x+dx[i]
#         new_y = y+dy[i]
#         if(can_go(new_x,new_y)):
#             visited[new_x][new_y] = True
#             dfs(new_x,new_y)

# dfs(0,0)
# if (flag == 0):
#     print(0)
q = deque()
def bfs():
    while q:
        cur_loc = q.popleft()
        if(cur_loc[0] == n-1 and cur_loc[1]== m-1):
            print(1)
            return
        for i in range(2):
            new_x = cur_loc[0]+dx[i]
            new_y = cur_loc[1]+dy[i]
            if(can_go(new_x,new_y)):
                visited[new_x][new_y] = True
                q.append((new_x,new_y))
    print(0)
q.append((0,0))
bfs()