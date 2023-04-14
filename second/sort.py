import sys

sys.stdin = open('second/inputsort.txt', 'rt')

input = sys.stdin.readline
s,e = map(int, input().split())

result = 0

for i in range(s, e+1):
    strr = str(i)
    result += sum(map(int, strr))


print(result)