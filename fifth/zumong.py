import sys
sys.stdin = open('fifth/inputzumong.txt', 'rt')

input = sys.stdin.readline

n = int(input().rstrip())
result = int(input().rstrip())
count = 0

A = list(map(int, input().split()))

for i in range(0, n):
    for j in range(n-1, i, -1):
        start = i
        end = j
        
        if result == A[start] + A[end]:
            count += 1
    

print(count)