from itertools import combinations

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

combis = list(combinations(points,m))

dists = []
for combi in combis:
    max = 0
    for i in range(0,(m-2)+1):
        x = (combi[i][0] - combi[i+1][0]) ** 2
        y = (combi[i][1] - combi[i+1][1]) ** 2
        result = x+y
        if(result > max):
            max = result
    dists.append(max)
    
    
print(min(dists))