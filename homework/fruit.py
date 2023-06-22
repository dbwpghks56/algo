# 모든 수가 자릿수들을 합한 뒤 빼면 9의 배수가 됨으로 9까지만 가져온다.
# 1~100 까지의 과일 중 9의 배수에 apple만 있기 때문
dt = {
    1: 'kiwi',
    2: 'pear',
    3: 'kiwi',
    4: 'banana',
    5: 'melon',
    6: 'banana',
    7: 'melon',
    8: 'pineapple',
    9: 'apple',
}

def fruit(n):
    # 1의 자리가 될 때까지 자릿수를 더하고 빼주는 과정을 반복한다.
    while n >= 10:
        digits_sum = sum(int(digit) for digit in str(n))
        n -= digits_sum
    
    # 해당하는 과일 반환
    return dt[n]
    
print(fruit(46))