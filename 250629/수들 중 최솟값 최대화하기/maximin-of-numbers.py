n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

selected_point = []
selected_col = []
answer = []

def choose(row, col):
    if (row == n):
        min = 10001
        
        for point in selected_point:
            x = point[0]
            y = point[1]
            
            if grid[x][y] < min:
                min = grid[x][y]
        answer.append(min)
        return
    
    for idx in range(n):
        if (idx in selected_col):
            continue
        selected_point.append((row, idx))
        selected_col.append(idx)
        choose(row+1, idx)
        selected_point.pop()
        selected_col.pop()


choose(0, -1)
print(max(answer))