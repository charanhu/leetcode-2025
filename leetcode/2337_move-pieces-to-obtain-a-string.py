class Solution(object):
    def canChange(self, start, target):
        """
        Determines if it is possible to transform the 'start' string into the 'target' string
        by moving 'L' pieces only to the left and 'R' pieces only to the right.
        
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        # If the two strings are not the same length, transformation is impossible.
        if n != len(target):
            return False
        
        # Remove underscores from both strings.
        # This ensures that the relative order of 'L' and 'R' pieces is identical.
        if start.replace("_", "") != target.replace("_", ""):
            return False

        # Initialize two pointers for start and target.
        i = 0  # Pointer for the start string.
        j = 0  # Pointer for the target string.

        # Process both strings until we reach the end.
        while i < n and j < n:
            # Skip underscores in the start string.
            while i < n and start[i] == "_":
                i += 1
            # Skip underscores in the target string.
            while j < n and target[j] == "_":
                j += 1

            # If both pointers have reached the end, break out of the loop.
            if i == n and j == n:
                break
            # If one pointer reaches the end before the other (should not happen as orders match),
            # then we exit.
            if i == n or j == n:
                break

            # Now both start[i] and target[j] are non-underscore characters (either 'L' or 'R').
            # They must be the same piece; if not, transformation is impossible.
            if start[i] != target[j]:
                return False

            # If the current character is 'L', it can only move left.
            # Thus, its index in start must be greater than or equal to its index in target.
            if start[i] == "L" and i < j:
                return False

            # If the current character is 'R', it can only move right.
            # Thus, its index in start must be less than or equal to its index in target.
            if start[i] == "R" and i > j:
                return False

            # Move both pointers to process the next non-blank character.
            i += 1
            j += 1

        # If all non-blank pieces satisfy the movement constraints, the transformation is possible.
        return True


# 2337. Move Pieces to Obtain a String
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

# The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
# The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
# Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

# Example 1:

# Input: start = "_L__R__R_", target = "L______RR"
# Output: true
# Explanation: We can obtain the string target from start by doing the following moves:
# - Move the first piece one step to the left, start becomes equal to "L___R__R_".
# - Move the last piece one step to the right, start becomes equal to "L___R___R".
# - Move the second piece three steps to the right, start becomes equal to "L______RR".
# Since it is possible to get the string target from start, we return true.
# Example 2:

# Input: start = "R_L_", target = "__LR"
# Output: false
# Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
# After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
# Example 3:

# Input: start = "_R", target = "R_"
# Output: false
# Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
 

# Constraints:

# n == start.length == target.length
# 1 <= n <= 105
# start and target consist of the characters 'L', 'R', and '_'.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 132.4K
# Submissions
# 232.1K
# Acceptance Rate
# 57.1%
# Topics
# Two Pointers
# String
# Companies
# 0 - 3 months
# Google
# 13
# Meta
# 3
# 0 - 6 months
# Amazon
# 3
# Microsoft
# 2
# Hint 1
# After some sequence of moves, can the order of the pieces change?
# Hint 2
# Try to match each piece in s with a piece in e.
# Similar Questions
# Valid Parentheses
# Easy
# Swap Adjacent in LR String
# Medium
# Discussion (118)