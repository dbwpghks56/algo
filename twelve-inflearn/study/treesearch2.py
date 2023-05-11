import sys

sys.stdin = open('twelve-inflearn/study/inputsearch2.txt', 'rt')
input = sys.stdin.readline

visited = []
n = int(input().rstrip())
A = list(map(int, input().split()))
r = int(input().rstrip())
graph = {}
count = 0
answer = 0
root = 0

for i in range(n):
    graph[i] = []

for i in A:
    if i in graph and count != r:
        graph[i].append(count)
        
    if i == -1:
        root = count
        
    count += 1

def dfs(cur_v):
    global answer
    visited.append(cur_v)
    if graph[cur_v] == []:
            answer += 1
    
    for v in graph[cur_v]:
        if v not in visited:                
            dfs(v)
        
    return answer
if r != root:
    print(dfs(root))
else:
    print(0)


