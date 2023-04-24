import sys
from collections import deque

sys.stdin = open('eight/switchqueue.txt', 'rt')
input = sys.stdin.readline

n, r = map(int, input().split())
myqueue = deque([i for i in range(1, n+1)])
A = list(map(int, input().split()))
result = 0

for i in range(r):
    s = A[i]
    if(myqueue[0] == s):
        myqueue.popleft()
        
    else:
        r2 = abs(myqueue.index(s) - 0)
        r3 = abs(len(myqueue)-1 - myqueue.index(s))
        if r2 > r3:
            for _ in range(r3+1):
                result += 1
                myqueue.rotate(1)
            myqueue.popleft()
        else:
            for _ in range(r2):
                result += 1
                myqueue.rotate(-1)
            myqueue.popleft()
print(result)
        