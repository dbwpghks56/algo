from collections import deque
import sys

sys.stdin = open('twelve-inflearn/study/inputsearch.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
row, col, ba = 0, 0, 0

def numIslands(grid):
    number_of_islands = 0
    n = len(grid)
    m = len(grid[0])
    
    def bfs(x, y):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        grid[x][y] = -1
        queue = deque() # = deque([(x,y)]) 로 가능
        queue.append((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i  in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if 0 <= next_x and next_x < n and 0 <= next_y and next_y < m:
                    if grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = -1
                        queue.append((next_x,next_y))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(i, j)
                number_of_islands += 1
            
    return number_of_islands

for _ in range(n):
    row, col, ba = map(int, input().split())

    grid = [[0] * row for _ in range(col)]
    for _ in range(ba):
        c, r = map(int, input().split())
        grid[r][c] = 1
    
    print(numIslands(grid))