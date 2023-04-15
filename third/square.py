import sys

sys.stdin = open('third/inputnemo.txt', 'rt')
input = sys.stdin.readline

x1, y1, x2 , y2 = map(int, input().split())

x3 = x2 - x1
y3 = y2 - y1

A = [x1, y1, x3, y3]

A.sort()

print(A[0])