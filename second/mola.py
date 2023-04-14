import sys

sys.stdin = open('second/inputmola.txt', 'rt')
input = sys.stdin.readline

p, w = map(int, input().split())

result = 0
numPad = [['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]

for c in list(input()):
    if c == ' ' :
        result += p
        continue
    for i in range(8):
        if c not in numPad[i]:
            continue
        if numPad[i].index(c) > 0:
            result += p + w
            break
        elif numPad[i].index(c) == 0:
            result += p
            break
print(result)