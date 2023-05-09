nums = [4, 1, 9, 7, 5, 3, 16]
target = 14
mydict = {}

def twoSum(nums, target):
    for n in nums:
        v = target - n
        if n in mydict:
            return True
        else:
            mydict[v] = 0
    return False

print(twoSum(nums=nums, target=target))