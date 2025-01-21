class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum, right_sum = 0, sum(nums)
        for pivote, num in enumerate(nums):
            right_sum-=num
            if left_sum==right_sum:
                return pivote
                break
            else:
                left_sum+=num
        return -1
        



# my sol
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
                break
        return -1

        