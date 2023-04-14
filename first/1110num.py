import sys

sys.stdin = open('first/input1110.txt', 'rt')

num = sys.stdin.readline().rstrip()
ten, il, count, total = 0, 0, 0, 0
print(num)
if(int(num) < 9):
    num = '0' + num
    
ten = int(num[0])
il = int(num[1])

while(1):
    count += 1
    
    if(str(ten) + str(il) == num):
        break

print(num)
print(ten)
print(il)
print(count)