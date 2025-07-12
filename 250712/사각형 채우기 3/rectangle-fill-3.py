MOD =  1000000007

n = int(input())
dp = [0 for _ in range(n+1)]
# Please write your code here.
dp[0] = 0
dp[1] = 2

for i in range(2,n+1):
    dp[i] = 3*dp[i-1] + 1
print(dp[n]%MOD)