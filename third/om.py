import sys

sys.stdin = open('third/inputom.txt', 'rt')
input = sys.stdin.readline

A = {"black": 1,
      "brown" : 10,
      "red" : 100,
      "orange" : 1000,
      "yellow" : 10000,
      "green" : 100000,
      "blue" : 1000000,
      "violet" : 10000000,
      "grey" : 100000000,
      "white" : 1000000000,
      }
count = 0
result = ""
resultt = 0

for i in range(3) :
    count = 0
    s = input().rstrip()

    if i != 2:
        for c in A.keys():

            if s == c:
                result += str(count)
                break

            count += 1

    else:
        for c in A.keys():

            if s == c:
                resultt = int(result) * A[c]
                break

print(resultt)