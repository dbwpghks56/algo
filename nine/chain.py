import sys

sys.stdin = open('nine/inputchain.txt', 'rt')
input = sys.stdin.readline

n = int(input().rstrip())
A = list(map(int, input().split()))
result = 0

def solve(s: list):
    

if n == 2 or n == 3:
    result = result + 1
    print(result)
    
else:
    