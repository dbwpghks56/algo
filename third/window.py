import sys
from collections import deque

sys.stdin = open('third/inputwindow.txt', 'rt')

input = sys.stdin.readline

n, w = map(int, input().split())
myqueue = deque()
A = list(map(int, input().split()))

for i in range(n):
    while myqueue and myqueue[-1][0] > A[i]:
        myqueue.pop()

    myqueue.append((A[i], i))

    if myqueue[0][1] <= i - w:
        myqueue.popleft()

    print(myqueue[0][0], end= ' ')