import sys
import math

sys.stdin = open('fifth/inputprime.txt', 'rt')
input = sys.stdin.readline

a, b = map(int, input().split())
count = 0
lists = []

if a == 2:
    count += 1

def mola(v):
    lists = []
    j = 2
    
    while j <= v:
        if v % j == 0:
            lists.append(j)
            v = v / j
        else:
            j += 1
    return lists

for i in range(a, b+1):
    listss = mola(i)
    if len(listss) != 1:
        listsss = mola(len(listss))
    
        if len(listsss) == 1:
            count += 1
    
print(count)