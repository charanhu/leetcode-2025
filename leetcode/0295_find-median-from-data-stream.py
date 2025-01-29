import heapq


class MedianFinder(object):

    def __init__(self):
        self.lowHalf = []
        self.highHalf = []

        self.num_addNum_call = 0
        self.num_findMedian_call = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.num_addNum_call <= 5 * (10**4):
            self.num_addNum_call += 1

            heapq.heappush(self.lowHalf, -num)

            if self.highHalf and (-self.lowHalf[0] > self.highHalf[0]):
                val = heapq.heappop(self.lowHalf)
                heapq.heappush(self.highHalf, -val)

            if len(self.lowHalf) < len(self.highHalf):
                val = heapq.heappop(self.highHalf)
                heapq.heappush(self.lowHalf, -val)

            elif len(self.lowHalf) > len(self.highHalf) + 1:
                val = heapq.heappop(self.lowHalf)
                heapq.heappush(self.highHalf, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        if self.num_findMedian_call <= 5 * (10**4):
            self.num_findMedian_call += 1

            totol_size = len(self.lowHalf) + len(self.highHalf)
            if totol_size == 0:
                return None
            if totol_size % 2 == 0:
                return (-self.lowHalf[0] + self.highHalf[0]) / 2.0
            else:
                return -self.lowHalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 295. Find Median from Data Stream
# Solved
# Hard
# Topics
# Companies
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 

# Constraints:

# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
 

# Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 924.5K
# Submissions
# 1.8M
# Acceptance Rate
# 52.8%
# Topics
# Two Pointers
# Design
# Sorting
# Heap (Priority Queue)
# Data Stream
# Companies
# 0 - 3 months
# Google
# 17
# Amazon
# 14
# Meta
# 6
# Uber
# 2
# Splunk
# 2
# Okta
# 2
# PayPal
# 2
# StackAdapt
# 2
# WorldQuant
# 2
# 0 - 6 months
# Pinterest
# 8
# Microsoft
# 6
# TikTok
# 3
# Anduril
# 3
# Docusign
# 3
# Apple
# 2
# IXL
# 2
# Tinder
# 2
# 6 months ago
# Oracle
# 11
# Bloomberg
# 8
# Adobe
# 5
# Citadel
# 5
# Nvidia
# 5
# Goldman Sachs
# 4
# Yahoo
# 3
# Flipkart
# 2
# Agoda
# 2
# Salesforce
# 2
# Similar Questions
# Sliding Window Median
# Hard
# Finding MK Average
# Hard
# Sequentially Ordinal Rank Tracker
# Hard
# Minimum Operations to Make Median of Array Equal to K
# Medium
# Minimum Operations to Make Subarray Elements Equal
# Medium
# Discussion (86)