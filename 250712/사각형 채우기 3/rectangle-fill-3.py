MOD =  1000000007

n = int(input())
dp = [0 for _ in range(n+1)]
# Please write your code here.
dp[0] = 0
dp[1] = 2
if(n>1):
    dp[2] = 7
for i in range(3,n+1):
    dp[i] = 4*dp[i-2] + 2*dp[i-1]
print(dp[n]%MOD)