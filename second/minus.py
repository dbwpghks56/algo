import sys

sys.stdin = open('second/inputminus.txt', 'rt')
input = sys.stdin.readline

strr = input().split("-")
answer = 0

def mySum(v):
    plustResult = 0
    plus = str(v).split("+")
    for c in plus:
        plustResult += int(c)
        
    return plustResult

for i in range(len(strr)):
    pp = mySum(strr[i])
    
    if i == 0 :
        answer += pp
        
    else:
        answer -= pp
    

print(answer)