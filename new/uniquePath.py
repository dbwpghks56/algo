# 일반적인 완전탐색
def dps(r, c):
    if r == 0 and c == 0:
        return 1
    uniquepath = 0

    if r -1 >= 0:
        uniquepath = dps(r-1, c)
    if c -1 >= 0:
        uniquepath = dps(r , c-1)

    return uniquepath

# 완전탐색 제외 dp 알고리즘 적용
# Top Down
dp = {}
def uniquePathAlgo(m,n):
    def dptd(r, c):
        if r == 0 and c == 0:
            dp[(r, c)] = 1
            return dp[(r, c)]
        uniquePath = 0
        if((r,c) not in dp):
            if r -1 >= 0:
                uniquePath += dptd(r-1, c)
            if c-1 >= 0:
                uniquePath += dptd(r, c-1)

            dp[(r,c)] = uniquePath
        
        return dp[(r,c)]
    print(dp)
    return dptd(m-1,n-1)
print(uniquePathAlgo(3,7))
# dp = [[-1] * n for _ in range(m)]

def uniquePathAlgoArray(m,n):
    dp = [[-1] * n for _ in range(m)]
    def dptd(r, c):
        if r == 0 and c == 0:
            dp[r][c] = 1
            return dp[r][c]
        
        uniquePath = 0

        if(dp[r][c] == -1):
            if r -1 >= 0:
                uniquePath += dptd(r-1, c)
            if c-1 >= 0:
                uniquePath += dptd(r, c-1)

            dp[r][c] = uniquePath
        
        return dp[r][c]
    print(dp)
    return dptd(m-1,n-1)

# Bottom Up 방식은 내가 짜볼 거임




print(uniquePathAlgoArray(3,7))










#
def uniquePathBootomUp(m,n):
    dp = [[-1] * n for _ in range(m)]

    for r in range(m):
        dp[r][0] = 1

    for c in range(n):
        dp[0][c] = 1

    for r in range(1,m):
        for c in range(1,n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    return dp[m-1][n-1]

print(uniquePathBootomUp(3,7))