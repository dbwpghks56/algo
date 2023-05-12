memo = {}
# top down 형식
def fipo(n):
    if n == 1 or n == 2:
        return 1
    
    if n not in memo:
        memo[n] = fipo(n-1) + fipo(n-2)
        
    return memo[n]

memo2 = {1 : 1, 2 : 1}
# bottom up 형식
def fipo2(n):
    if n == 1 or n == 2: # 베이스 케이스가 있기 때문에 이 조건문은 없어도 됨
        return 1
    
    for i in range(n):
        memo2[i] = memo2[i-1] + memo2[i-2]
        
    return memo2[n]