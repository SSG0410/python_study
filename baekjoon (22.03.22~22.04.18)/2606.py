#dfs
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

n = int(input())
m = int(input())
graph = [[]*n for i in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)

print(visited.count(True)-1)