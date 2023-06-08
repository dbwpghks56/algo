import sys
sys.stdin = open('CodingTestStudy/pelin.txt', 'rt')
input = sys.stdin.readline

def is_pelin(st):
    return st == st[::-1]

while True:
    n = input().rstrip()
    if n == "0" : break
    print( "yes" if is_pelin(n) else "no" )
    