import sys
from collections import deque

sys.stdin = open('CodingTestStudy/searchMaze.txt', 'rt')
input = sys.stdin.readline

r, c = map(int, input().split())
A = [[] * c for _ in range(r)]
visited = []

for i in range(r):
    A[i] = list(input().rstrip())
print(A)
def bfs(grid):
    shortestPathLen = 0
    row = r
    col = c
    
    def bfs(x, y,sl):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        grid[x][y] = "0"
        queue = deque()
        queue.append((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if 0 <= next_x and next_x < r and 0 <= next_y and next_y < c:
                    if grid[next_x][next_y] == "1":
                        sl += 1
                        grid[next_x][next_y] = "0"
                        queue.append((next_x, next_y))

        return sl

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                shortestPathLen = bfs(i,j, shortestPathLen)
                
    print(grid)
    return shortestPathLen



print(bfs(A))