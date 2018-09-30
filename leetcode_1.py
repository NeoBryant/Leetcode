class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            if (target-num) in nums and nums.index(target-num)!=i:
                    return [i,nums.index(target-num)]
