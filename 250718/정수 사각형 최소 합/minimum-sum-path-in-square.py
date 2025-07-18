n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
def Print(arr):
    for r in arr:
        print(r)
    print()
def init():
    dp[0][n-1] = grid[0][n-1]
    for i in range(n-2,-1,-1):
        dp[0][i] = grid[0][i] + dp[0][i+1]
    for i in range(1,n):
        dp[i][n-1] = grid[i][n-1] + dp[i-1][n-1]
        
init()

for r in range(1,n):
    for c in range(n-2,-1,-1):
        dp[r][c] = min(grid[r][c]+dp[r][c+1], grid[r][c]+dp[r-1][c])
        
print(dp[n-1][0])
        