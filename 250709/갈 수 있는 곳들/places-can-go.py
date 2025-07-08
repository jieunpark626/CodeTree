from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
visited_node = set()
answer = 0

def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def can_go(x,y): 
    return x>=0 and x<n and y>=0 and y<n and grid[x][y] == 0 and visited[x][y] == False

def bfs():
    global answer
    while q:
        cur_loc = q.popleft()

        for i in range(4):
            new_x = cur_loc[0] + dx[i]
            new_y = cur_loc[1] + dy[i]
            
            if(can_go(new_x, new_y)):
                visited[new_x][new_y] = True
                q.append((new_x,new_y))
                visited_node.add((new_x,new_y))

for point in points:
    r, c= point[0]-1,point[1]-1
    
    q.append((r, c))
    init_visited()
    visited[r][c] = True
    visited_node.add((r,c))
    bfs()
    
print(len(visited_node))
