dp = {}
def stair(n):
    # 한 번에 오를 수 있는 계단이 1, 2 이기 때문에 n이 1, 2 일때 해당하는 값을 반환해준다.
    # 최소 코스트라면 n 이 아니라 1을 반환해주면 됨
    if n == 1 or n == 2:
        return n
    
    # dp 를 이용해 같은 연산은 다시 하지 않고 dp에 저장된 값을 사용한다.
    if n not in dp:
        dp[n] = stair(n-1) + stair(n-2)
    
    return dp[n]

print(stair(5))