MOD = 10007

n = int(input())

cnt = [0 for _ in range(n+1)]
cnt[0] = 1

for i in range(n+1):
    if i+2 <= n:
        cnt[i+2] = (cnt[i+2]+cnt[i]) % MOD
    if i+3 <= n:
        cnt[i+3] += (cnt[i+3]+cnt[i]) % MOD

print(cnt[n])
