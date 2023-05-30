# import sys
# from collections import deque

# sys.stdin = open('CodingTestStudy/bomul.txt', 'rt')
# input = sys.stdin.readline

# r,c = map(int, input().split())
# A = [[] * c for _ in range(r)]

# for i in range(r):
#     A[i] = list(input().rstrip())

# maxs = 0
# def bomul(grid):
#     numofland = 0
#     def bfs(x, y):
#         global maxs
#         grid[x][y] = 'W'
#         delta = [(0,1), (1,0), (-1,0), (0,-1)]
#         queue = deque()
#         queue.append((x,y,1))
        
#         while(queue):
#             cur_x, cur_y, cur_l = queue.popleft()
            
#             for dx, dy in delta:
#                 next_x = cur_x + dx
#                 next_y = cur_y + dy
                
#                 if 0 <= next_x and next_x < r and 0 <= next_y and next_y < c:
#                     if grid[next_x][next_y] == 'L':
#                         grid[next_x][next_y] = 'W'
#                         cur_l += 1
#                         queue.append((next_x, next_y, cur_l))
#                         maxs = max(maxs, cur_l)
    
#     for i in range(r):
#         for j in range(c):
#             if A[i][j] == "L":
#                 bfs(i,j)
#                 numofland = max(numofland, maxs -1 )
                
#     return numofland

# print(bomul(A))

from collections import deque
import sys

sys.stdin = open('CodingTestStudy/bomul.txt', 'rt')
input = sys.stdin.readline

def bfs():
    global maxs
    while q:
        i,j,c = q.popleft()
        c+=1
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0<=nx<n and 0<=ny<m and not vist[nx][ny] and s[nx][ny]=='L':
                vist[nx][ny] = True
                q.append([nx,ny,c])
                maxs = max(maxs,c)

n,m= map(int,input().split())
s =[]
for i in range(n):
    s2 = sys.stdin.readline()
    s.append(s2)

dx  =[1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
re = 0
for i in range(n):
    for j in range(m):
        if s[i][j]=='L':
            maxs = 0
            q.append([i,j,1])
            vist = [[False]*m for _ in range(n)]
            vist[i][j] = True
            bfs()
            re = max(re,maxs-1)
print(re)
