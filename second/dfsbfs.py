import sys
from collections import deque

sys.stdin = open('second/inputdfsbfs.txt', 'rt')
input = sys.stdin.readline

n, m ,s = map(int, input().split())
A = [[] for _ in range(n + 1)]


for _ in range(m):
    s2, e = map(int, input().split())
    A[s2].append(e)
    A[e].append(s2)
    
for i in range(n + 1):
    A[i].sort()

def DFS(v):
    print(v, end= ' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
visited = [False] * (n + 1)
DFS(s)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
print()
visited = [False] * (n + 1)
BFS(s)