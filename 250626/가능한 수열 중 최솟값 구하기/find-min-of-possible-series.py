n = int(input())

answer = [0 for _ in range(n)]


def Print(answer):
    for item in answer:
        print(item, end="")


def check(idx, arr):
    for length in range(1, (idx + 1) // 2 + 1): 
        for start in range(max(0, idx - 2 * length + 1), idx - length + 1):
            first = arr[start:start + length]
            second = arr[start + length:start + 2 * length]
            if first == second:
                return False
    return True


suc = False


def dfs(idx):
    global suc

    if (idx == n):
        suc = True
        Print(answer)
        return
    for i in range(4, 7):
        if (idx > 0 and (answer[idx-1] == i)):
            continue
        answer[idx] = i

        if (idx > 2 and not check(idx, answer[0:idx+1])):  # 4개 이상부터
            continue
        dfs(idx+1)
        if (suc):
            return


dfs(0)
