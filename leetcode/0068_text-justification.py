class Solution(object):
    def fullJustify(self, words, maxWidth):
        # Initialize the result list to store each justified line.
        res = []
        # 'i' is the index of the first word in the current line.
        i = 0
        # 'n' is the total number of words.
        n = len(words)
        
        # Process all words.
        while i < n:
            # 'j' will be used to find the last word that can fit in the current line.
            j = i
            # 'line_len' stores the total length of words (without spaces) in the current line.
            line_len = 0  
            
            # Try to fit as many words as possible into the current line.
            # (j - i) counts the minimum spaces required between words.
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                # Add the length of the current word to line_len.
                line_len += len(words[j])
                # Move to the next word.
                j += 1
            
            # Calculate the number of gaps between words in the current line.
            # If only one word, gap_count will be 0.
            gap_count = j - i - 1  
            
            # Check if this line is the last line or if it contains only one word.
            if j == n or gap_count == 0:
                # Join all words with a single space.
                line = " ".join(words[i:j])
                # Pad the end of the line with spaces to ensure its length is maxWidth.
                line += " " * (maxWidth - len(line))
            else:
                # Calculate the total number of spaces that must be inserted in this line.
                total_spaces = maxWidth - line_len
                # 'base_spaces' is the minimum number of spaces to insert between each pair of words.
                base_spaces = total_spaces // gap_count
                # 'extra_spaces' is the remainder that will be distributed one extra space at a time from the left.
                extra_spaces = total_spaces % gap_count
                # Start building the line as an empty string.
                line = ""
                # Loop over all words except the last one in the current line.
                for k in range(i, j - 1):
                    # Append the current word.
                    line += words[k]
                    # Calculate how many spaces to add after the current word.
                    # Add one extra space if this gap is among the first 'extra_spaces' gaps.
                    spaces_to_add = base_spaces + (1 if k - i < extra_spaces else 0)
                    # Append the calculated number of spaces.
                    line += " " * spaces_to_add
                # Append the last word in the current line (no spaces are added after it).
                line += words[j - 1]
            
            # Append the constructed line to the result list.
            res.append(line)
            # Set 'i' to 'j' to process the next line starting from the next word.
            i = j
        
        # Return the list of justified lines.
        return res



# 68. Text Justification
# Solved
# Hard
# Topics
# Companies
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
 

# Constraints:

# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 503K
# Submissions
# 1.1M
# Acceptance Rate
# 46.7%
# Topics
# Array
# String
# Simulation
# Companies
# 0 - 3 months
# Google
# 14
# Anyscale
# 9
# Uber
# 8
# Karat
# 6
# Capital One
# 5
# BCG
# 5
# Amazon
# 4
# Apple
# 3
# TikTok
# 3
# Airbnb
# 2
# 0 - 6 months
# Roblox
# 11
# Moveworks
# 6
# Databricks
# 5
# Bloomberg
# 3
# SIG
# 3
# Sentry
# 3
# Meta
# 2
# Microsoft
# 2
# Visa
# 2
# Atlassian
# 2
# 6 months ago
# Zoho
# 7
# Coursera
# 7
# Adobe
# 5
# Samsara
# 4
# Oracle
# 3
# Robinhood
# 3
# Yahoo
# 3
# Twilio
# 3
# LinkedIn
# 2
# Walmart Labs
# 2
# Similar Questions
# Rearrange Spaces Between Words
# Easy
# Divide a String Into Groups of Size k
# Easy
# Split Message Based on Limit
# Hard
# Discussion (149)