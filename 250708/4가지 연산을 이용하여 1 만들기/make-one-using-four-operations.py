from collections import deque

N = int(input())

q = deque()
visited = deque()

def bfs():
    while q:
        num, cnt = q.popleft()

        if (num == 1):
            print(cnt)
            return
        
        if (num % 3 == 0 and (num//3) not in visited):
            q.append((num//3, cnt+1))
            visited.append(num//3)
        if (num % 2 == 0 and (num//2) not in visited):
            q.append((num // 2, cnt+1))
            visited.append(num//2)
        if ((num-1) not in visited):
            q.append((num-1, cnt+1))
            visited.append(num-1)
        if ((num+1) not in visited):
            q.append((num+1, cnt+1))
            visited.append(num+1)

q.append((N, 0))
visited.append(N)

bfs()
