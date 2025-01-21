class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]
    

    # my solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current={}
        for i, num in enumerate(nums):
            if num in current:
                count=current[num]
                current[num]=count+1
            else:
                current[num]=1
        max_v=0
        max_val_key=0
        for k, v in current.items():
            if v>max_v:
                max_v=v
                max_val_key=k
        return max_val_key


        