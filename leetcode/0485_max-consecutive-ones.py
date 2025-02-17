class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize two counters:
        # current_count tracks the number of consecutive 1's in the current window.
        # max_count stores the maximum number of consecutive 1's found so far.
        current_count = 0
        max_count = 0
        
        # Iterate through each number in the list.
        for num in nums:
            # If the current number is 1, we are in a window of consecutive ones.
            if num == 1:
                current_count += 1  # Increase the count for the current window.
            else:
                # When a 0 is encountered, the window of consecutive 1's ends.
                # Update max_count if the current window is larger.
                max_count = max(max_count, current_count)
                # Reset the current_count for the next window of 1's.
                current_count = 0
        
        # After the loop, check one last time in case the array ends with a 1.
        max_count = max(max_count, current_count)
        
        # Return the maximum window length of consecutive 1's.
        return max_count


        


# 485. Max Consecutive Ones
# Solved
# Easy
# Topics
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.5M
# Submissions
# 2.5M
# Acceptance Rate
# 61.6%
# Topics
# Array
# Companies
# 0 - 3 months
# Google
# 13
# Meta
# 4
# Amazon
# 3
# Microsoft
# 2
# Bloomberg
# 2
# 0 - 6 months
# Accenture
# 2
# Yandex
# 2
# 6 months ago
# Adobe
# 6
# Uber
# 4
# Apple
# 3
# tcs
# 2
# Oracle
# 2
# Hint 1
# You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window. How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.
# Similar Questions
# Max Consecutive Ones II
# Medium
# Max Consecutive Ones III
# Medium
# Consecutive Characters
# Easy
# Longer Contiguous Segments of Ones than Zeros
# Easy
# Length of the Longest Alphabetical Continuous Substring
# Medium
# Maximum Enemy Forts That Can Be Captured
# Easy
# Discussion (66)