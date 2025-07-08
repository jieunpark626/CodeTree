from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
answer = 1

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
                answer += 1
                
for point in points:
    q.append(point)
    visited[point[0]][point[1]] = True
    bfs()

print(answer)
