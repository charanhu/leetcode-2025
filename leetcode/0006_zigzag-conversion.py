# METHOD - 1
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there is only one row, or if the number of rows is greater than or equal
        # to the length of the string, then the zigzag conversion doesn't change the string.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings to represent each row in the zigzag pattern.
        # Initially, all rows are empty.
        row = [''] * numRows
        
        # currentRow keeps track of the current row index we are filling.
        # step is used to determine the direction: 1 means moving down, -1 means moving up.
        currentRow = 0
        step = 1
        
        # Iterate over each character in the string.
        for char in s:
            # Append the current character to the corresponding row.
            row[currentRow] += char
            
            # If we are at the first row, we should start moving downwards.
            if currentRow == 0:
                step = 1
            # If we are at the last row, we should move upward.
            elif currentRow == numRows - 1:
                step = -1
                
            # Move to the next row according to the current direction.
            currentRow += step
        
        # Finally, join all rows together to form the resulting string.
        return ''.join(row)


# METHOD 2
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Special case: if there's only one row, no conversion is needed.
        if numRows == 1:
            return s

        # Create a list of lists, where each inner list represents a row.
        # We use numRows lists because there will be that many rows.
        rows = [[] for _ in range(numRows)]

        # 'i' is the current row index; 'd' is the direction:
        #   d = 1 means moving downwards, d = -1 means moving upwards.
        i = 0
        d = 1

        # Iterate over each character in the input string.
        for char in s:
            # Append the current character to the appropriate row.
            rows[i].append(char)
            
            # If we are at the first row, we must start moving downwards.
            if i == 0:
                d = 1
            # If we are at the last row, we must start moving upwards.
            elif i == numRows - 1:
                d = -1
            
            # Move to the next row in the current direction.
            i += d

        # Build the final result by concatenating all the rows.
        res = ""
        for row in rows:
            res += "".join(row)
        return res




# 6. Zigzag Conversion
# Solved
# Medium
# Topics
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.6M
# Submissions
# 3.2M
# Acceptance Rate
# 50.6%
# Topics
# String
# Companies
# 0 - 3 months
# Google
# 12
# Amazon
# 11
# Zopsmart
# 8
# Meta
# 4
# Bloomberg
# 2
# Salesforce
# 2
# 0 - 6 months
# Microstrategy
# 5
# PayPal
# 3
# Microsoft
# 2
# Mitsogo
# 2
# 6 months ago
# Zoho
# 9
# Adobe
# 8
# Apple
# 8
# Uber
# 8
# Yahoo
# 6
# Oracle
# 5
# ServiceNow
# 5
# carwale
# 4
# ConsultAdd
# 4
# Cisco
# 3
# Discussion (375)