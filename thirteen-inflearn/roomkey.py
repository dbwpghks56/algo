from collections import deque

rooms = [[1,3],[2,4],[0],[4],[],[3,4]]
visited = {}

def bfs(start_v):
    visited[start_v] = start_v
    queue = deque([start_v])
    while queue:
        cur_v = queue.popleft()
        for v in rooms[cur_v]:
            if v not in visited:
                visited[v] = start_v
                queue.append(v)
                
    return visited

def dfs(cur_v):
    visited[cur_v] = cur_v
    for v in rooms[cur_v]:
        if v not in visited:
            dfs(v)
            
    return visited

print(bfs(0))
visited = {}
print(dfs(0))