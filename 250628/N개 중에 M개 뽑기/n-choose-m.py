N, M = map(int, input().split())

# Please write your code here.
N, M = map(int, input().split())

def Print(arr):
    for num in arr:
        print(num, end=" ")
    print()

nums = []
def dfs(cur_num, idx):
    if(cur_num == M+1):
        Print(nums)
    for i in range(idx, N+1):
        nums.append(i)
        dfs(cur_num+1, i+1)
        nums.pop()

dfs(1,1)
        