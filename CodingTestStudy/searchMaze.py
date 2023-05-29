import sys
from collections import deque

sys.stdin = open('CodingTestStudy/searchMaze.txt', 'rt')
input = sys.stdin.readline

r, c = map(int, input().split())
A = [[] * c for _ in range(r)]
visited = []

for i in range(r):
    A[i] = list(input().rstrip())

def bfs(grid, sl):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0,1))
    if grid[0][0] != "1" or grid[r-1][c-1] != "1":
        return sl
    grid[0][0] = "0"
    while queue:
        cur_x, cur_y, cur_l = queue.popleft()

        if cur_x == r-1 and cur_y == c-1:
            sl = cur_l
            break

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if 0 <= next_x and next_x < r and 0 <= next_y and next_y < c:
                if grid[next_x][next_y] == "1":
                    grid[next_x][next_y] = "0"
                    queue.append((next_x, next_y, cur_l+1))

            if next_x == r and next_y == c:
                return sl

    return sl



print(bfs(A, 1))