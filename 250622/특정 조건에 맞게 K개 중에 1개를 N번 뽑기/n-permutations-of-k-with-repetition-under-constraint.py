K, N = map(int, input().split())

combination = []

def Print():
    
    for item in combination:
        print(item, end=" ")
    print()
    return

def Choose(idx):
    if (idx == N):
        Print()
        return
    for i in range(1,K+1):
        if(idx <2 or combination[idx-1] != i or combination[idx-2] != i):
            combination.append(i)
            Choose(idx+1)
            combination.pop()

Choose(0)
        
        