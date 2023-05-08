import sys

sys.stdin = open('ten/inputtwosum.txt', 'rt')

input = sys.stdin.readline

target = int(input().rstrip())
nums = list(map(int, input().split()))

def twoSum(nums, target):
    left = 0
    right = len(nums)-1
    
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
            
        elif nums[left] + nums[right] < target:
            left += 1
            
        else:
            return True
        
    return False

nums.sort()
print(twoSum(nums= nums, target=target))