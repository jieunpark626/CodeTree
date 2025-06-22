n, m, k = map(int, input().split())  # n : 턴 수, m : 판, k: 말의 수
nums = list(map(int, input().split()))

arr = []
hscore = [1] * k  # 각 말의 위치

# idx = 턴 수
answer = 0
def Cal():
    score = 0
    for item in hscore:
        score += (item>=m)
    return score

def Choose(idx):
    global answer
    
    answer = max(answer, Cal())
    if (idx == n):
        return

    for i in range(k):
        if (hscore[i] >= m):
            continue
        arr.append(i)
        hscore[i] += nums[idx]
        Choose(idx+1)
        hscore[i] -= nums[idx]
        arr.pop()


Choose(0)
print(answer)
