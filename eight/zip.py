import sys

sys.stdin = open('eight/inputzip.txt', 'rt')
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]

for i in range(n+1):
    A[i].append(i)

for i in range(m):
    finds, n1, n2 = map(int, input().split())
    
    if finds == 0:
        if [n1] in A:
            A[A.index([n1])].append(n2)
            A.remove([n2])
            print(A)
        
    else:
        if [1, 3] in A:
            print("yes")