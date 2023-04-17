import sys

sys.stdin = open('fifth/inputgoldsilver.txt', 'rt')
open = sys.stdin.readline

m, r = map(int, input().split())
A = [[] for _ in range(m)]

for i in range(m):
    A[i] = list(map(int, input().split()))
    print(A)

for i in range(m):
    if r == A[i][0] :
        r = i
        break
    
print(r)
