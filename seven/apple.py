import sys

sys.stdin = open('seven/inputapple.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
A = [[] for _ in range(n)]
sumA = [[0] for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

for i in range(n):
    temp = 0
    for data in A[i]:
        temp = temp + data
        sumA[i].append(temp)
        
for i in range(len(sumA) - 1):
        for j in range(len(sumA[0])):
            sumA[i + 1][j] += sumA[i][j]

for i in range(len(sumA)):
    print(sumA[i])
    
for i in range(len(sumA)):
    