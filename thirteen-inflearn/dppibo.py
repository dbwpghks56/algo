memo = {}

def fipo(n):
    if n == 1 or n == 2:
        return 1
    
    if n not in memo:
        memo[n] = fipo(n-1) + fipo(n-2)
        
    return memo[n]