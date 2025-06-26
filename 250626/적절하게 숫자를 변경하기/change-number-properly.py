N, M = map(int, input().split())  # N: 길이, M: 비슷한 수열
a = list(map(int, input().split()))
comb = []


def check(arr):
    cnt = 0
    for start in range(0, len(arr)-1):
        if (arr[start] != arr[start+1]):
            cnt += 1
    if (cnt <= M):
        return True
    else:
        return False


def Sim(arr):
    global a
    cnt = 0
    for i in range(len(a)):
        if (a[i] == arr[i]):
            cnt += 1
    
    return cnt

maxSim = 0
def combination():
    global maxSim
    if (len(comb) == N):
        sim = Sim(comb)
        if (maxSim < sim):
            maxSim = sim
        return

    for i in range(1, 5):
        comb.append(i)
        if not check(comb):
            comb.pop()
            continue
        combination()
        comb.pop()
    return


combination()
print(maxSim)
