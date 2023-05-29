cost = [10, 15, 20, 17, 1]
memo = {}

# Top down 방식
def dp(n):
    if n == 0 or n == 1:
        return 0
    if n not in memo:
        memo[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
    print(memo)
    return memo[n]

# bottom up
def dpB(n):
    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 0
    
    for i in range(2, n + 1):
        memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
    print(memo)
    return memo[n]

print(dp(len(cost)))
print(dpB(len(cost)))