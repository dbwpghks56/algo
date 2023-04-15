import sys

sys.stdin = open('third/inputnemo.txt', 'rt')
input = sys.stdin.readline

c, r = map(int, input().split())
A = [[] for _ in range(c)]

for i in range(c):
    A[i] = list(map(int, input().rstrip()))

for i in range(c):
    for j in range(r):
        if i == j:
            print(A[i][j])
