nums = [3,2,4]
target = 6

class Solution:
    def twoSum(nums, target):
        dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict:
                return [dict[diff], i]
            dict[num] = i
        return


    
Solution.twoSum(nums, target)