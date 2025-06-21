op = []  # 연산자
nums = []  # 숫자


expression = input()

for i in range(len(expression)):
    if (i % 2 == 1):  # 짝수면
        op.append(expression[i])
    else:
        nums.append(expression[i])


N = len(nums)

calNums = []  # 계산할 숫자


def Cal():
    numArr = calNums.copy()

    for i in range(len(op)):
        if (op[i] == "+"):
            numArr[i+1] = numArr[i]+numArr[i+1]
        elif (op[i] == "-"):
            numArr[i+1] = numArr[i]-numArr[i+1]
        elif (op[i] == "*"):
            numArr[i+1] = numArr[i]*numArr[i+1]

    return numArr[N-1]


answer = 0


def Backtracking():
    global answer
    if (len(calNums) == N):
        result = Cal()
        if (result > answer):
            answer = result
        return

    for i in range(1, 5):
        calNums.append(i)
        Backtracking()
        calNums.pop()


Backtracking()
print(answer)
