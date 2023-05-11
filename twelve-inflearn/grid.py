from collections import deque

visited = []
"""
def bfs(start_v, graph):
    visited.append(start_v)
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
            
    return visited
"""

def numIslands(grid):
    number_of_islands = 0
    n = len(grid)
    m = len(grid[0])
    
    def bfs(x, y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        grid[x][y] = "-1"
        queue = deque() # = deque([(x,y)]) 로 가능
        queue.append((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i  in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if 0 <= next_x and next_x < n and 0 <= next_y and next_y < m:
                    if grid[next_x][next_y] == "1":
                        grid[next_x][next_y] = "-1"
                        queue.append((next_x,next_y))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                bfs(i, j)
                number_of_islands += 1
            
    return number_of_islands

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(numIslands(grid))
print(grid)