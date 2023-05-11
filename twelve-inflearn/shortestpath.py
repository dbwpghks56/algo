from collections import deque

def bfs(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    
    delta = [
        (1,0),(-1,0),(0,1),(0,-1),
        (1,1),(1,-1),(-1,1),(-1,-1)
    ]

    myq = deque([(0, 0, 1)])
    if grid[0][0] != 0 or grid[row-1][col-1] != 0:
        return shortest_path_len
    
    grid[0][0] = -1
    
    
    while myq:
        cur_x, cur_y, cur_l = myq.popleft()
        
        if cur_x == col-1 and cur_y == row-1:
            shortest_path_len = cur_l
            break
            
        for dx, dy in delta:
            next_x = cur_x + dx
            next_y = cur_y + dy
            
            if 0 <= next_x and next_x < col and 0 <= next_y and next_y < row:
                if grid[next_y][next_x] == 0:
                    grid[next_y][next_x] = -1
                    myq.append((next_x, next_y, cur_l + 1))
            
            if next_x == col and next_y == row:
                return shortest_path_len
            
    return shortest_path_len


grid = [
    [0,0,0,1,0,0,0],
    [0,1,1,1,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,0,1,1,1,0],
    [0,1,0,0,0,0,0]
]

print(bfs(grid))