import sys
input=sys.stdin.readline

def dfs(x, y):
    if x>=n or y>=n or visited[x][y]==True:
        return
    visited[x][y]=True
    if graph[x][y]==-1:
        return
    dfs(x, y+graph[x][y])
    dfs(x+graph[x][y], y)

n=int(input())
graph=[list(map(int, input().split())) for i in range(n)]
visited=[[False]*n for i in range(n)]

dfs(0, 0)

if visited[n-1][n-1]==True:
    print('HaruHaru')
else:
    print('Hing')