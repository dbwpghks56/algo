import sys
from collections import deque

sys.stdin = open("CodingTestStudy/algospot.txt", "rt")
input = sys.stdin.readline

c, r = map(int, input().split())
A = [[] * c for _ in range(r)]

for i in range(r):
    A[i] = list(input().rstrip())
    
    
def bfs(grid):
    sl = -1
    delta = [(0,1), (1,0),(-1,0),(0,-1)]
    queue = deque()
    queue.append((0,0,0))
    grid[0][0] = '-1'
    while queue:
        curx, cury, curl = queue.popleft()
        
        if curx == r-1 and cury == c-1:
            sl = curl
            break
        
        for dx, dy in delta:
            nextx = curx + dx
            nexty = cury + dy
            if 0 <= nextx and nextx < r and 0 <= nexty and nexty < c:
                if(grid[nextx][nexty] != '-1'):
                    if(grid[nextx][nexty] == "1"):
                        queue.append((nextx, nexty, curl + 1))
                    else:
                        queue.append((nextx, nexty, curl))
                    grid[nextx][nexty] = '-1'
            if nextx == r and nexty == c:
                return sl
    
    return sl
    
print(bfs(A))