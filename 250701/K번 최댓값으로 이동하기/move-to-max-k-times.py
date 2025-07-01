from collections import deque
n,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
start_x, start_y = map(int,input().split())
start_x -= 1
start_y -= 1
dx = (-1,0,1,0)
dy = (0,1,0,-1)
visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()

max = 0
max_loc = (n,n)

def init_visit():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            
            
def can_go(x,y,num):
    return x>=0 and x<n and y>=0 and y<n and visited[x][y] == False and grid[x][y]<num
def bfs(cur_num):
    global max
    global max_loc
    
    while q:
        cur_loc = q.popleft()
        if(grid[cur_loc[0]][cur_loc[1]] < cur_num and grid[cur_loc[0]][cur_loc[1]] >= max):
            if(grid[cur_loc[0]][cur_loc[1]] > max):
                max = grid[cur_loc[0]][cur_loc[1]]
                max_loc = (cur_loc[0],cur_loc[1])
            if(cur_loc[0]<max_loc[0] or (cur_loc[0] == max_loc[0] and cur_loc[1]<max_loc[1])):
                max = grid[cur_loc[0]][cur_loc[1]]
                max_loc = (cur_loc[0],cur_loc[1])

        for i in range(4):
            new_x, new_y = cur_loc[0]+dx[i], cur_loc[1]+dy[i]
            if(can_go(new_x,new_y,cur_num)):
                visited[new_x][new_y] = True
                q.append((new_x,new_y))


def sol():
    global max, max_loc, start_x, start_y
    for i in range(k):
        max = 0
        max_loc = (n,n)
        init_visit()
        q.append((start_x,start_y))    
        bfs(grid[start_x][start_y])
        if(max == 0):
            print(start_x+1, start_y+1)
            return
        start_x,start_y = max_loc[0],max_loc[1]
    
    print(max_loc[0]+1, max_loc[1]+1)
    
sol()