from collections import deque

n = int(input())

cnt = [0 for _ in range(n+1)]
q = deque()


def dp():
    while q:
        cur = q.popleft()
        if(cur+2<=n):
            cnt[cur+2] += cnt[cur]
            q.append(cur+2)
        if(cur+3<=n):
            cnt[cur+3]+= cnt[cur]
            q.append(cur+3)
        
q.append(0)
cnt[0] = 1
dp()
print(cnt[n])
