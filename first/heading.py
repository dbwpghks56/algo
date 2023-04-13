import sys

sys.stdin = open('first/input.txt', 'rt')

sizeNo, qNo = map(int, sys.stdin.readline().split())

listData = list(map(int, sys.stdin.readline().split()))
sumData = [0]
temp = 0

for data in listData:
    temp = temp + data
    sumData.append(temp)

for quiz in range(qNo):
    first, second = map(int, sys.stdin.readline().split())
    print(sumData[second] - sumData[first-1])

