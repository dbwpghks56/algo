import sys

sys.stdin = open('fifth/inputmunza.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
d = {}

for _ in range(n):
    c = input().rstrip()
    
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
A = [k for k,v in d.items() if max(d.values()) == v]
A.sort()
print(A[0])