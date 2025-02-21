class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        INT_MAX = 2**31 - 1
        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            if rev > INT_MAX:
                return 0
            x = x // 10
        return sign * rev
    

# 7. Reverse Integer
# Solved
# Medium
# Topics
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3.8M
# Submissions
# 12.9M
# Acceptance Rate
# 29.8%
# Topics
# Math
# Companies
# Similar Questions
# String to Integer (atoi)
# Medium
# Reverse Bits
# Easy
# A Number After a Double Reversal
# Easy
# Count Number of Distinct Integers After Reverse Operations
# Medium
# Discussion (480)