import sys

sys.stdin = open('eight/inputhap.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
mydict = dict()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(n):
    mydict[A[i]] = B[i]
sorted_dict = sorted(mydict.items())
print(sorted_dict)

print(sorted_dict.pop())