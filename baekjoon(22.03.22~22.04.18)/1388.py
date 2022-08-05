import sys
input = sys.stdin.readline

def dfs(x, y):
    if x<-1 or x>=n or y<-1 or y>=m:
        return False
    if visited[x][y]==True:
        return False
    visited[x][y]=True
    if graph[x][y]=='-' and (y==m-1 or graph[x][y+1]=='-'):
        dfs(x, y+1)
    elif graph[x][y]=='|' and (x==n-1 or graph[x+1][y]=='|'):
        dfs(x+1, y)
    return True

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
visited = [[False]*m for i in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            count+=1

print(count)