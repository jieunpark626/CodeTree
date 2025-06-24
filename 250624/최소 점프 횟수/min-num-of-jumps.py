n = int(input()) # 노드 수
num = list(map(int,input().split()))

def dfs(node):
    if(node == n-1): # 끝에 도달
        return 0
    if(num[node] == 0): # 끝에 도달하지 않았는데 멈추면
        return -1 # 실패
    
    result = []    
    for i in range(1,num[node]+1):
        child = dfs(node+i)
        if(child == -1):
            continue
        result.append(dfs(node+i)+1)
    if not result:
        return -1
    return min(result)



print(dfs(0))
