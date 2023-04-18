import sys
sys.setrecursionlimit(10000)
sys.stdin = open('six/inputrank.txt', 'rt')
input = sys.stdin.readline

roomNumber, roomLimit = map(int, input().split())
rooms = {0 : []}
flag = True

def mola(roomss:dict, users: list, i : int):
    if i not in roomss:
        roomss[i] = [users]
        return
    low = int(roomss[i][0][0]) - 10
    large = int(roomss[i][0][0]) + 10
    
    if low <= int(users[0]) and large >= int(users[0]) and len(roomss[i]) < 5:
        roomss.get(i).append(users)
        return
    else:
        mola(roomss,users, i + 1)

for _ in range(roomNumber):
    user = list(input().split())
    if flag:
        rooms[0].append(user)
    
    else:
        mola(rooms, user, 0)
                
    flag = False
    
for i in range(len(rooms.keys())):
    rooms[i].sort(key= lambda x : x[1])
    if len(rooms[i]) == 5:
        print("Started!")
        
    elif len(rooms[i]) < 5:
        print("Waiting!")
    
    for c in rooms[i]:
        print(c[0], c[1])