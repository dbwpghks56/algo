def solution(park, routes):
    answer = []
    row = 0
    col = 0
    dt = {"E": (0,1), "S": (1,0), "W": (0,-1), "N": (-1,0)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                row = i
                col = j
    
    for route in routes:
        direct = route.split()[0]
        value = route.split()[1]
        next_r, next_c = dt[direct]
        
        next_r = row + (next_r * int(value))
        next_c = col + (next_c * int(value))
        
        if(0<= next_r < len(park) and 0 <= next_c < len(park[0])):
            if(park[next_r][next_c] != "X"):
                row = next_r
                col = next_c
        
    answer.append(row)
    answer.append(col)
    return answer


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]	))