n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False for _ in range(n)] for _ in range(n)]

total_vil_num = 0
people_num = 0
people_nums = []

def can_go(x,y):
    return x>=0 and x<n and y>=0 and y<n and visited[x][y] is False and grid[x][y] == 1

def dfs(x,y):
    global people_num
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if(can_go(new_x,new_y)):
            visited[new_x][new_y] = True
            people_num += 1
            dfs(new_x,new_y)

def sol():
    global people_num
    global total_vil_num
    for i in range(n):
        for j in range(n):
            if(can_go(i,j)):
                visited[i][j] = True
                total_vil_num += 1
                people_num = 1
                dfs(i,j)
                people_nums.append(people_num)
sol()
people_nums.sort()           
print(total_vil_num)
for item in people_nums:
    print(item)
            