class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        max_num_distinct, current=0, -float('inf')
        for num in nums:
            l, h = num-k, num+k
            if current < l:
                current=l
                max_num_distinct+=1
            elif current < h:
                current+=1
                max_num_distinct+=1
        return max_num_distinct

        
