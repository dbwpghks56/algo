import sys

sys.stdin = open('third/inputnum.txt', 'rt')

input = sys.stdin.readline

n = int(input())
listNum = list(map(int, input().split()))
listNum.sort()
result = 0

for k in range(n):
    target = listNum[k]
    i = 0
    j = n - 1

    while i < j:
        if listNum[i] + listNum[j] == target:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif listNum[i] +listNum[j] < target:
            i += 1
        else:
            j -= 1
print(result)

