n = int(input())

dp = [0 for _ in range(20)]
dp[1] = 1
dp[2] = 2
# Please write your code here.
if(n>=3):
    for i in range(1,n):
        dp[n] += dp[i] 

    dp[n] += dp[n-1]

print(dp[n])
 