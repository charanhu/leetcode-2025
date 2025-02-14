# METHOD 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        for number, count in freq.items():
            bucket[count].append(number)
        res = []
        for i in range(n, 0, -1):
            if bucket[i]:
                res.extend(bucket[i])
                if len(res) >= k:
                    return res[:k]
        return res

        





# METHOD 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_c = {}
        for n in nums:
            if n in freq_c:
                freq_c[n]+=1
            else:
                freq_c[n]=1
        
        res=sorted_items = sorted(freq_c.items(), key=lambda x: x[1], reverse=True)

        final_res = []
        for r in res:
            final_res.append(r[0])
        return final_res[:k]



# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.6M
# Submissions
# 4.1M
# Acceptance Rate
# 64.0%
# Topics
# Array
# Hash Table
# Divide and Conquer
# Sorting
# Heap (Priority Queue)
# Bucket Sort
# Counting
# Quickselect
# Companies
# 0 - 3 months
# Meta
# 51
# Amazon
# 22
# Google
# 13
# Microsoft
# 8
# Apple
# 3
# Goldman Sachs
# 3
# Uber
# 3
# Oracle
# 2
# Chewy
# 2
# Microstrategy
# 2
# 0 - 6 months
# Bloomberg
# 5
# TikTok
# 4
# Avito
# 3
# Intuit
# 2
# Salesforce
# 2
# 6 months ago
# Adobe
# 13
# Yahoo
# 7
# Netflix
# 6
# Walmart Labs
# 5
# Tesla
# 5
# Yandex
# 4
# PayPal
# 4
# Cisco
# 2
# Pinterest
# 2
# Siemens
# 2
# Similar Questions
# Word Frequency
# Medium
# Kth Largest Element in an Array
# Medium
# Sort Characters By Frequency
# Medium
# Split Array into Consecutive Subsequences
# Medium
# Top K Frequent Words
# Medium
# K Closest Points to Origin
# Medium
# Sort Features by Popularity
# Medium
# Sender With Largest Word Count
# Medium
# Most Frequent Even Element
# Easy
# Linked List Frequency
# Easy
# Discussion (228)