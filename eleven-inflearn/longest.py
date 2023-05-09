nums = []
numsdict = {}

def longest(nums) -> int:
    longestn = 0
    for num in nums:
        numsdict[num] = 0
        #numsset = set(nums) value를 사용하지 않을 거면 이 방식도 가능
        
    for num in numsdict:
        if num -1 not in numsdict:
            cnt = 1
            target = num + 1

            while target in numsdict:
                target += 1
                cnt += 1
                
            longestn = max(longestn, cnt)
    return longestn

print(longest(nums=[6,7,10,5,4,2,11,12,13,14]))