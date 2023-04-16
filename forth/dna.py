import sys

sys.stdin = open('forth/inputdna.txt', 'rt')

input = sys.stdin.readline

cr = ["A", "G", "C", "T"]
datas = [["A", "C", "A", "G"],
         ["C", "G", "T", "A"],
         ["A", "T", "C", "G"],
         ["G", "A", "G", "T"]]
c = 0
r = 0
n = int(input().rstrip())
A = list(input().rstrip())

for i in range(n - 1, -1, -1):
    p = datas[cr.index(A[i])][cr.index(A[i-1])]
    A[i-1] = p


print(A[0])