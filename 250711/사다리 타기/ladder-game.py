n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

result = [0 for _ in range(n+1)]  # 사다리 결과
max_floor = 0

# edge 갯수만큼 돌아감

def find_max_floor():
    global max_floor
    for edge in edges:
        if edge[1] > max_floor:
            max_floor = edge[1]

# a: 세로 줄, b: 몇번째 위치
def ride(a, b, edge_arr):
    if (b == max_floor + 1):
        return int(a)
    if (a, b) in edge_arr:
        return ride(a+1, b+1, edge_arr)
    elif (a-1, b) in edge_arr:
        return ride(a-1, b+1, edge_arr)
    else:
        return ride(a, b+1, edge_arr)

def init():
    find_max_floor()
    for i in range(1, n+1):
        num = int(ride(i, 1, edges))
        result[num] = i
        
comb = []
selected_edges = []
def combinations(n, idx):
    if len(comb) == n:
        tmp = comb.copy()
        selected_edges.append(tmp)
    for i in range(idx, len(edges)):
        comb.append(edges[i])
        combinations(n, i+1)
        comb.pop()

def sol():
    global comb,selected_edges,result,n
    for i in range(0,m+1):
        comb.clear()
        selected_edges.clear()
        combinations(i,0)
        tmp_result = [0 for _ in range(n+1)]
        for e in selected_edges:
            for i in range(1, n+1):
                num = int(ride(i, 1, e))
                tmp_result[num] = i
            if (tmp_result == result):
                print(len(e))
                return    

init()
sol()