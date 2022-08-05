import sys
from collections import deque
input = sys.stdin.readline

#dfs
def dfs(graph, v, dfs_visited):
    dfs_visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if dfs_visited[i]==False:
            dfs(graph, i, dfs_visited)

#bfs
def bfs(graph, v, bfs_visited):
    bfs_visited[v]=True
    queue=deque([v])
    while queue:
        temp=queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if bfs_visited[i]==False:
                queue.append(i)
                bfs_visited[i]=True

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
dfs_visited = [False for i in range(n+1)]
bfs_visited = [False for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)