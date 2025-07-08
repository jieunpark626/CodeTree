from collections import deque

N = int(input())

q = deque()

def bfs():
    while q:
        cur_num_cnt = q.popleft()

        if(cur_num_cnt[0] == 1):
            print(cur_num_cnt[1])
            return
        
        if(cur_num_cnt[0]%3 == 0):
            q.append((int(cur_num_cnt[0] / 3), cur_num_cnt[1]+1))
        elif(cur_num_cnt[0]%2==0):
            q.append((int(cur_num_cnt[0] / 2), cur_num_cnt[1]+1))
        else:
            q.append((cur_num_cnt[0] - 1, cur_num_cnt[1]+1))
            q.append((cur_num_cnt[0] + 1, cur_num_cnt[1]+1))

q.append((N,0))
bfs()
