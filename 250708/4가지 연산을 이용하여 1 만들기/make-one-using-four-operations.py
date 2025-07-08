from collections import deque

N = int(input())

q = deque()


def bfs():
    while q:
        cur_num_cnt = q.popleft()
        
        if(cur_num_cnt[0] == 1):
            print(cur_num_cnt[1])
            break
        for i in range(4):
            if (i == 0):
                q.append((cur_num_cnt[0] - 1, cur_num_cnt[1]+1))
            elif (i == 1):
                q.append((cur_num_cnt[0] + 1, cur_num_cnt[1]+1))
            elif (i == 2 and cur_num_cnt[0] % 2 == 0):
                q.append((cur_num_cnt[0] / 2, cur_num_cnt[1]+1))
            elif (i == 3 and cur_num_cnt[0] % 3 == 0):
                q.append((cur_num_cnt[0] / 3, cur_num_cnt[1]+1))

q.append((N,0))
bfs()
        
        