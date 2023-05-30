import sys
from collections import deque

sys.stdin = open("CodingTestStudy/findcity.txt", "rt")
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = dict()
visited = []

for i in range(n):
    graph[i+1] = []

for i in range(m):
    node, next = map(int, input().split())
    if node not in graph:
        graph[node] = [next]
        
    else:
        graph[node].append(next)
count = 0
def bfs(start_v):
    answer = [-1] * (n+1)
    answer[start_v] = 0
    visited.append(start_v)
    queue = deque()
    queue.append(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if answer[v] == -1:
                answer[v] = answer[cur_v] + 1
                queue.append(v)
        
    if k not in answer:
        print(-1)
    else:
        for i in range(n+1):
            if answer[i] == k:
                print(i)
bfs(x)
