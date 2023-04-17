import sys
sys.stdin = open('fifth/inputpocketmon.txt', 'rt')

input = sys.stdin.readline
n, m = map(int, input().split())
A = []
graph = {}
for i in range(1, n+1):
    a = input().strip()
    graph[i] = a
    graph[a] = i

for j in range(m):
    ask = input().strip()
    if ask.isdigit():
        print(graph[int(ask)])
    else:
        print(graph[ask])