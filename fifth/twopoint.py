import sys

sys.stdin = open('fifth/twopoint.txt', 'rt')
input = sys.stdin.readline

n, r = map(int, input().split())

A = list(map(int, input().split()))
count = 0
s = 0
e = 0
sum = 0
# 동적 구간 합...?
while (s < n) :
    if (sum == r):
        count += 1
        sum -= A[s]
        s+=1
    elif (sum > r or e == n):
        sum -= A[s]
        s+=1
    else:
        sum += A[e]
        e+=1

print(count)