class Solution(object):
    # The main function that searches for the first occurrence of 'needle' in 'haystack'
    # using the Knuth-Morris-Pratt (KMP) algorithm.
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # If the haystack is empty, there's nowhere to search, so return -1.
        if not haystack:
            return -1
        # If the needle is empty, per this implementation, we return -1.
        # (Note: Some problems may define an empty needle to return 0, but here we choose -1.)
        if not needle:
            return -1
        
        # Preprocess the needle to build the Longest Prefix Suffix (LPS) array.
        # The LPS array helps us skip unnecessary comparisons.
        lps = self.build_lps(needle)
        
        # Initialize two pointers:
        # i for the current index in haystack
        # j for the current index in needle
        i, j = 0, 0
        
        # Loop through the haystack until we reach its end.
        while i < len(haystack):
            # If the characters at the current pointers match, move both pointers forward.
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                # If j reaches the length of needle, it means we've found the complete needle in haystack.
                if j == len(needle):
                    # The starting index of the found substring is (i - j).
                    return i - j
            else:
                # If a mismatch occurs and j > 0, we use the LPS array to avoid rechecking characters.
                if j > 0:
                    # Reset j to the LPS value of the previous character.
                    # This tells us the next best position in the needle to compare.
                    j = lps[j - 1]
                else:
                    # If j is already at 0, there is no prefix to fall back to,
                    # so simply move to the next character in haystack.
                    i += 1
        # If we exit the loop without finding a match, return -1.
        return -1

    # Helper function to build the Longest Prefix Suffix (LPS) array for the pattern (needle).
    # The LPS array at each index i contains the length of the longest proper prefix of the substring needle[0:i+1]
    # that is also a suffix of this substring.
    def build_lps(self, pattern):
        # Create an LPS list of the same length as the pattern, initialized to 0.
        lps = [0] * len(pattern)
        
        # 'length' keeps track of the length of the previous longest prefix-suffix.
        # We start with the second character (index 1) since the LPS for the first character is always 0.
        i, length = 1, 0
        
        # Loop over the pattern to calculate the LPS value for each position.
        while i < len(pattern):
            # If the current character matches the character at the 'length' index,
            # we have found a longer prefix that is also a suffix.
            if pattern[i] == pattern[length]:
                length += 1          # Increase the length of the current matching prefix.
                lps[i] = length      # Set the LPS value for index i.
                i += 1               # Move to the next character in the pattern.
            else:
                # If there is a mismatch and length is not zero,
                # then we set length to the LPS of the previous character,
                # effectively "falling back" to the last known smaller prefix.
                if length != 0:
                    length = lps[length - 1]
                    # Note: We do not increment i here because we want to compare the same i with the updated length.
                else:
                    # If length is 0, then no proper prefix matches the suffix ending at i,
                    # so we set LPS for i to 0 and move to the next character.
                    lps[i] = 0
                    i += 1
        # Return the completed LPS array.
        return lps



# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 3M
# Submissions
# 6.9M
# Acceptance Rate
# 44.2%
# Topics
# Two Pointers
# String
# String Matching
# Companies
# 0 - 3 months
# Google
# 16
# Meta
# 5
# Microsoft
# 5
# Amazon
# 4
# Bloomberg
# 4
# tcs
# 3
# Expedia
# 2
# 6 months ago
# Apple
# 17
# Adobe
# 12
# Uber
# 12
# Yahoo
# 10
# Warnermedia
# 5
# Zoho
# 3
# Accenture
# 3
# IBM
# 2
# Infosys
# 2
# LinkedIn
# 2
# Similar Questions
# Shortest Palindrome
# Hard
# Repeated Substring Pattern
# Easy
# Discussion (325)