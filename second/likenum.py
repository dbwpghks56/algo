import sys

sys.stdin = open('second/inputnum.txt', 'rt')

input = sys.stdin.readline
dn = int(input())
listData = list(map(int, input().split()))
listData.sort()
tn = int(input())
targetData = list(map(int, input().split()))

for i in range(tn):
    flag = False
    target = targetData[i]
    
    start = 0
    end = len(listData) - 1
    
    while start <= end:
        midi = int((start + end) / 2)
        midv = listData[midi]
        
        if midv < target:
            start = midi + 1
            
        elif midv > target:
            end = midi - 1
            
        else:
            flag = True
            break
    if flag:
        print(1)
        
    else:
        print(0)
