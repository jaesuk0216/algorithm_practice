import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

parent = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    start,end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(root) :
    for neighbor in graph[root] :
        if(parent[neighbor] == 0) :
            parent[neighbor] = root
            dfs(neighbor)

dfs(1)

for i in range(2, n+1) :
    print(parent[i])
    