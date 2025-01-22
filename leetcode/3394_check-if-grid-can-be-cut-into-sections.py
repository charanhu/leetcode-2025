class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        def can_make_two_cuts(intervals):
            # Sort intervals by starting point
            intervals.sort(key=lambda x: x[0])
            gaps = 0
            current_end = intervals[0][1]

            # Look for gaps between intervals
            for start, end in intervals[1:]:
                if start >= current_end:  # found a gap
                    gaps += 1
                    if gaps == 2:
                        return True
                        break
                current_end = max(current_end, end)
            return False

        # Prepare x-axis intervals for vertical cut check
        x_intervals = [(rect[0], rect[2]) for rect in rectangles]
        if can_make_two_cuts(x_intervals):
            return True

        # Prepare y-axis intervals for horizontal cut check
        y_intervals = [(rect[1], rect[3]) for rect in rectangles]
        if can_make_two_cuts(y_intervals):
            return True

        return False


# 3394. Check if Grid can be Cut into Sections
# Solved
# Medium
# Topics
# Companies
# Hint
# You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

# (startx, starty): The bottom-left corner of the rectangle.
# (endx, endy): The top-right corner of the rectangle.
# Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

# Each of the three resulting sections formed by the cuts contains at least one rectangle.
# Every rectangle belongs to exactly one section.
# Return true if such cuts can be made; otherwise, return false.

 

# Example 1:

# Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

# Output: true

# Explanation:



# The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

# Example 2:

# Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

# Output: true

# Explanation:



# We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

# Example 3:

# Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

# Output: false

# Explanation:

# We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

 

# Constraints:

# 3 <= n <= 109
# 3 <= rectangles.length <= 105
# 0 <= rectangles[i][0] < rectangles[i][2] <= n
# 0 <= rectangles[i][1] < rectangles[i][3] <= n
# No two rectangles overlap.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 9.3K
# Submissions
# 22.8K
# Acceptance Rate
# 40.8%
# Topics
# Array
# Sorting
# Companies
# 0 - 3 months
# Google
# 10
# Hint 1
# For each rectangle, consider ranges [start_x, end_x] and [start_y, end_y] separately.
# Hint 2
# For x and y directions, check whether we can split it into 3 parts.
# Discussion (21)