dt = {}
def solution(n):
    if n == 1 or n == 2:
        return 1
    
    if n not in dt:
        dt[n] = solution(n-1) + solution(n-2)
    
    return dt[n]

print(solution(3))