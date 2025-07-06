from collections import deque

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range (n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()
melted_ice_num = 0

def Print(arr):
    for row in arr:
        print(row)

def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def can_go(x,y):
    return x>=0 and x<n and y>=0 and y<m and visited[x][y] == False

def bfs():
    global melted_ice_num
    
    while q:
        cur_loc = q.popleft()
        
        for i in range(4):
            new_x = cur_loc[0] + dx[i]
            new_y = cur_loc[1] + dy[i]
            
            if not can_go(new_x,new_y):
                continue
            
            if(grid[new_x][new_y] == 0): # 물인 경우
                visited[new_x][new_y] = True
                q.append((new_x,new_y))
            elif(grid[new_x][new_y] == 1):
                melted_ice_num += 1
                visited[new_x][new_y] = True
                grid[new_x][new_y] = 0


answer = 0
while True:
    prev_melted_ice_num = melted_ice_num
    melted_ice_num = 0
    init_visited()
    q.append((0,0))
    bfs()

    if melted_ice_num == 0:
        print(answer,prev_melted_ice_num)
        break
    
    answer += 1
            