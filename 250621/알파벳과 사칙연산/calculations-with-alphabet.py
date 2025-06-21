op = []  # 연산자
nums = []  # 숫자


expression = input()

for i in range(len(expression)):
    if (i % 2 == 1):  # 짝수면
        op.append(expression[i])
    else:
        if not (expression[i] in nums):
            nums.append([expression[i], 0])

N = len(nums)

calNums = []  # 계산할 숫자

def findNum(expression):
    for i in range(len(nums)):
        if (nums[i][0] == expression):
            return nums[i][1]


def Cal():
    preNum = findNum(expression[0])
    for i in range(len(expression)):
        if (i % 2 == 1):
            if (expression[i] == "+"):
                preNum = preNum + findNum(expression[i+1])
            elif (expression[i] == "-"):
                preNum = preNum - findNum(expression[i+1])
            elif (expression[i] == "*"):
                preNum = preNum * findNum(expression[i+1])
    return preNum

answer = float('-inf')

def Backtracking(idx):
    global answer
    if (idx == N):
        result = Cal()
        
        if (result > answer):
            answer = result
        
        return

    for i in range(1, 5):
        nums[idx][1] = i
        Backtracking(idx+1)
        nums[idx][1] = 0
    return


Backtracking(0)
print(answer)
