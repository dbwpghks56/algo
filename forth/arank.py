import sys

sys.stdin = open("forth/inputa.txt", "rt")
input = sys.stdin.readline
r, c = map(int, input().split())
A = [[] for _ in range(r)]

for i in range(r):
    A[i] = list(map(int, input().split()))
sumA= [[0], [0]]


for i in range(r):
    temp = 0
    for data in A[i]:
        temp = temp + data
        sumA[i].append(temp)
        
for i in range(len(sumA) - 1):
        for j in range(len(sumA[0])):
            sumA[i + 1][j] += sumA[i][j]

n = int(input().rstrip())
for _ in range(n):
    result = 0
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        print(A[x2-1][y2-1])
        continue
    
    print(sumA[x2-1][y2] - sumA[x1][y1-1])