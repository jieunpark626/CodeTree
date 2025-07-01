n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
# Please write your code here.
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    
answer = 0
def dfs(node):
    global answer
    for next in graph[node]:
        if visited[next] is False:
            visited[next] = True
            answer += 1
            dfs(next)
visited[1] = True
dfs(1)
print(answer)