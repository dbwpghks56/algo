import sys

sys.stdin = open('first/inputGold.txt', 'rt')

sizeNo, qNo, cNo = map(int, sys.stdin.readline().split())
listData = []
for _ in range(sizeNo):
    listData.append(int(sys.stdin.readline().rstrip()))
    
sumData = [0]
temp = 0

for data in listData:
    temp = temp + data
    sumData.append(temp)
print(sumData)
print(listData)
for quiz in range(qNo + cNo):
    typo, idxs, value = map(int, sys.stdin.readline().split())
    if typo == 1:
        temp = 0
        sumData = [0]
        listData[idxs-1] = value
        for data in listData:
            temp = temp + data
            sumData.append(temp)
            
    if typo == 2:
        print(sumData[value] - sumData[idxs-1])




