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



# # 28. Find the Index of the First Occurrence in a String
# # Solved
# # Easy
# # Topics
# # Companies
# # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# # Example 1:

# # Input: haystack = "sadbutsad", needle = "sad"
# # Output: 0
# # Explanation: "sad" occurs at index 0 and 6.
# # The first occurrence is at index 0, so we return 0.
# # Example 2:

# # Input: haystack = "leetcode", needle = "leeto"
# # Output: -1
# # Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# # Constraints:

# # 1 <= haystack.length, needle.length <= 104
# # haystack and needle consist of only lowercase English characters.
# # Seen this question in a real interview before?
# # 1/5
# # Yes
# # No
# # Accepted
# # 3M
# # Submissions
# # 6.9M
# # Acceptance Rate
# # 44.2%
# # Topics
# # Two Pointers
# # String
# # String Matching
# # Companies
# # 0 - 3 months
# # Google
# # 16
# # Meta
# # 5
# # Microsoft
# # 5
# # Amazon
# # 4
# # Bloomberg
# # 4
# # tcs
# # 3
# # Expedia
# # 2
# # 6 months ago
# # Apple
# # 17
# # Adobe
# # 12
# # Uber
# # 12
# # Yahoo
# # 10
# # Warnermedia
# # 5
# # Zoho
# # 3
# # Accenture
# # 3
# # IBM
# # 2
# # Infosys
# # 2
# # LinkedIn
# # 2
# # Similar Questions
# # Shortest Palindrome
# # Hard
# # Repeated Substring Pattern
# # Easy
# # Discussion (325)

# Below is a detailed step-by-step trace of the KMP algorithm (as implemented in your code) using an example. We’ll use:

# - **Haystack:** `"abxabcabcaby"`
# - **Needle:** `"abcaby"`

# The algorithm works in two phases:  
# 1. **Preprocessing (Building the LPS Array) for the Needle**  
# 2. **Searching for the Needle in the Haystack**

# ---

# ### 1. Building the LPS (Longest Prefix Suffix) Array

# The LPS array tells us the length of the longest proper prefix of the needle that is also a suffix up to each position. For the needle `"abcaby"` (indices 0 to 5), the process is:

# - **Index 0:**  
#   - Character: `'a'`  
#   - LPS: `0` (by definition, the first character always has an LPS value 0)

# - **Index 1:**  
#   - Characters: `"ab"`  
#   - Compare: needle[1] = `'b'` with needle[0] = `'a'` → **mismatch**  
#   - LPS[1] = `0`

# - **Index 2:**  
#   - Characters: `"abc"`  
#   - Compare: needle[2] = `'c'` with needle[0] = `'a'` → **mismatch**  
#   - LPS[2] = `0`

# - **Index 3:**  
#   - Characters: `"abca"`  
#   - Compare: needle[3] = `'a'` with needle[0] = `'a'` → **match**  
#   - Increase length to 1 and set LPS[3] = `1`

# - **Index 4:**  
#   - Characters: `"abcab"`  
#   - Compare: needle[4] = `'b'` with needle[1] = `'b'` (because current length is 1) → **match**  
#   - Increase length to 2 and set LPS[4] = `2`

# - **Index 5:**  
#   - Characters: `"abcaby"`  
#   - Compare: needle[5] = `'y'` with needle[2] = `'c'` → **mismatch**  
#   - Since length ≠ 0, update length = LPS[length - 1] = LPS[1] = `0`  
#   - Now compare needle[5] = `'y'` with needle[0] = `'a'` → **mismatch**  
#   - Set LPS[5] = `0`

# **Resulting LPS array:**  
# `[0, 0, 0, 1, 2, 0]`

# ---

# ### 2. Searching the Needle in the Haystack

# Initialize two pointers:
# - `i` for the haystack (starting at 0)
# - `j` for the needle (starting at 0)

# We then iterate through the haystack while comparing characters:

# | **Step** | **i** | **j** | **haystack[i]** | **needle[j]** | **Action** |
# |----------|-------|-------|-----------------|---------------|------------|
# | 1        | 0     | 0     | `'a'`         | `'a'`       | **Match:** Increment both `i` and `j` (i → 1, j → 1) |
# | 2        | 1     | 1     | `'b'`         | `'b'`       | **Match:** Increment both (i → 2, j → 2) |
# | 3        | 2     | 2     | `'x'`         | `'c'`       | **Mismatch:** Since `j > 0`, set `j = LPS[j-1]` = LPS[1] = `0` |
# | 4        | 2     | 0     | `'x'`         | `'a'`       | **Mismatch:** `j` is 0 so increment `i` (i → 3) |
# | 5        | 3     | 0     | `'a'`         | `'a'`       | **Match:** Increment both (i → 4, j → 1) |
# | 6        | 4     | 1     | `'b'`         | `'b'`       | **Match:** Increment both (i → 5, j → 2) |
# | 7        | 5     | 2     | `'c'`         | `'c'`       | **Match:** Increment both (i → 6, j → 3) |
# | 8        | 6     | 3     | `'a'`         | `'a'`       | **Match:** Increment both (i → 7, j → 4) |
# | 9        | 7     | 4     | `'b'`         | `'b'`       | **Match:** Increment both (i → 8, j → 5) |
# | 10       | 8     | 5     | `'c'`         | `'y'`       | **Mismatch:** Since `j > 0`, update `j = LPS[j-1]` = LPS[4] = `2` |
# | 11       | 8     | 2     | `'c'`         | `'c'`       | **Match:** Increment both (i → 9, j → 3) |
# | 12       | 9     | 3     | `'a'`         | `'a'`       | **Match:** Increment both (i → 10, j → 4) |
# | 13       | 10    | 4     | `'b'`         | `'b'`       | **Match:** Increment both (i → 11, j → 5) |
# | 14       | 11    | 5     | `'y'`         | `'y'`       | **Match:** Increment both (i → 12, j → 6) |

# - **Termination:**  
#   At step 14, `j` equals the length of the needle (6). This means a full match of the needle was found in the haystack.  
#   The starting index of the match is calculated as `i - j` = `12 - 6` = **6**.

# ---

# ### Final Outcome

# The needle `"abcaby"` is found in the haystack `"abxabcabcaby"` starting at index **6**.

# This detailed trace shows both how the LPS array is constructed and how the search uses it to efficiently match the needle against the haystack by avoiding unnecessary rechecks upon mismatches.

# Below is a detailed step-by-step backtracking (trace) of the KMP algorithm for the given example:

# - **Haystack:** `"sadbutsad"`
# - **Needle:** `"sad"`

# We'll walk through two phases: building the LPS (Longest Prefix Suffix) array for the needle, and then using it to search for the needle in the haystack.

# ---

# ## 1. Building the LPS Array for `"sad"`

# The LPS array captures, for each index, the length of the longest proper prefix that is also a suffix of the substring ending at that index.

# 1. **Index 0:**  
#    - **Character:** `'s'`  
#    - **LPS Value:** `0`  
#      (By definition, the first character always gets an LPS of 0.)

# 2. **Index 1:**  
#    - **Characters Considered:** `"sa"`  
#    - **Comparison:** Compare `needle[1]` (`'a'`) with `needle[0]` (`'s'`).  
#    - **Result:** Mismatch → **LPS[1] = 0**

# 3. **Index 2:**  
#    - **Characters Considered:** `"sad"`  
#    - **Comparison:** Compare `needle[2]` (`'d'`) with `needle[0]` (`'s'`).  
#    - **Result:** Mismatch → **LPS[2] = 0**

# **Final LPS Array:**  
# ```
# [0, 0, 0]
# ```

# *Observation:*  
# For `"sad"`, there are no proper prefixes that are also suffixes (other than the trivial case), so all values remain 0.

# ---

# ## 2. Searching for `"sad"` in `"sadbutsad"`

# We initialize two pointers:
# - **`i`** for the haystack (starts at 0)
# - **`j`** for the needle (starts at 0)

# We'll iterate through the haystack while comparing characters:

# | **Step** | **i** | **j** | **haystack[i]** | **needle[j]** | **Action** |
# |----------|-------|-------|-----------------|---------------|------------|
# | 1        | 0     | 0     | `s`             | `s`           | **Match:** Increment both pointers → `i=1`, `j=1` |
# | 2        | 1     | 1     | `a`             | `a`           | **Match:** Increment both pointers → `i=2`, `j=2` |
# | 3        | 2     | 2     | `d`             | `d`           | **Match:** Increment both pointers → `i=3`, `j=3` |

# - **Match Found:**  
#   At step 3, pointer `j` equals the length of the needle (3).  
#   The starting index of the match is calculated as:  
#   ```
#   start index = i - j = 3 - 3 = 0
#   ```

# Thus, the algorithm finds the first occurrence of `"sad"` in `"sadbutsad"` at index **0**.

# ---

# ## Recap of the Process

# 1. **LPS Construction:**  
#    For the needle `"sad"`, we computed the LPS array as `[0, 0, 0]` since no proper prefix is also a suffix in this pattern.

# 2. **KMP Search:**  
#    - The algorithm started comparing from the beginning of the haystack.
#    - Each character (`'s'`, `'a'`, `'d'`) matched in sequence.
#    - Upon matching the entire needle (when `j` reached 3), the algorithm returned the starting index, which is `0`.

# This backtracking shows how the KMP algorithm efficiently finds the match with minimal backtracking, using the precomputed LPS array to avoid redundant comparisons.