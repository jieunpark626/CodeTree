from itertools import combinations

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

combis = list(combinations(points, m))

dists = []
for combi in combis:
    max = 0
    items = list(combinations(combi, 2))
    for item in items:
        x = (item[0][0] - item[1][0]) ** 2
        y = (item[0][1] - item[1][1]) ** 2
        result = x+y
        if (result > max):
            max = result
    dists.append(max)

print(min(dists))
