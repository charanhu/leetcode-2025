class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = []
        for i in range(len(nums)):
            if nums[i] in complement:
                return [nums.index(target - nums[i]), i]
            complement.append(target - nums[i])
