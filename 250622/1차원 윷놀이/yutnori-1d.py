n, m, k = map(int, input().split())  # n : 턴 수, m : 판, k: 말의 수
nums = list(map(int, input().split()))

arr = []
hscore = [0] * k # 각 말의 위치

# idx = 턴 수
answer = 0
def Choose(idx,score):
    global answer
    if (idx == n):
        if(answer<score):
            answer = score
        return

    for i in range(k):
        if(hscore[i] >= m):
            continue
        
        arr.append(i)
        hscore[i] += nums[idx]
        if(hscore[i]>=m):
            score+=1
        Choose(idx+1,score)
        arr.pop()


Choose(0,0)
print(answer)
