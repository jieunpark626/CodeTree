n = int(input())
def Print(answer):
    for item in answer:
        print(item,end="")

answer = [0 for _ in range(n)]
def check(idx, arr):
    num = int((idx+1)/2)
    for j in range(2,num+1):
        num2 = j
        for i in range(0,idx-(2*num2)+2):
            if(arr[i:num2] == arr[num2:num2+num2]):
                return False
    
    return True

suc = False

def dfs(idx):
    global suc

    if(idx == n):
        suc = True
        Print(answer)
        return
    for i in range(4,7):
        if(idx>0 and (answer[idx-1] == i)):
            continue
        answer[idx] = i
        if(idx>2 and not check(idx,answer[0:idx+1])): #4개 이상부터
            continue
        dfs(idx+1)
        answer[idx] = 0
        if(suc):
            return
    return
dfs(0)
