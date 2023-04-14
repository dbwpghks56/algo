import sys
sys.setrecursionlimit(10000)
sys.stdin = open('second/insertnode.txt', 'rt')
input = sys.stdin.readline

node, edge = map(int, input().split())

A = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
            
for _ in range(edge):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
print(A)
count = 0

for i in range(1, node+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)

