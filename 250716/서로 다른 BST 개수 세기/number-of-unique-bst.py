n = int(input())

dp = [0 for _ in range(20)]
dp[0] = 1
dp[1] = 1
dp[2] = 2
# Please write your code here.

for i in range(3,n+1):
    for j in range(1,i+1):
        dp[i] += dp[j-1] * dp[i-j]

print(dp[n])
 