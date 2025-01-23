class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        merged=[]
        intervals.sort()
        merged.append(intervals[0])

        for start, end in intervals[1:]:
            if start<=merged[-1][1]:
                merged[-1][1]=max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

        
        # n=len(intervals)
        # p1=0
        # p2=p1+1
        # # intervals=list(map(lambda sort))
        # intervals.sort(key=lambda x: x[0])
        # while p1<n and p2<n and n>=1 and n<=10**4:
        #     start_p1, end_p1= intervals[p1][0], intervals[p1][1]
        #     start_p2, end_p2= intervals[p2][0], intervals[p2][1]
        #     if end_p1>=start_p2 and end_p1<=end_p2:
        #         intervals[p1:p2+1]=[[start_p1, end_p2]]
        #         n-=1
        #     elif start_p2>=start_p1 and end_p2<=end_p1:
        #         intervals[p1:p2+1]=[[start_p1, end_p1]]
        #         n-=1
        #     else:
        #         p1+=1
        #         p2+=1
        # return intervals

# 56. Merge Intervals
# Solved
# Medium
# Topics
# Companies
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.9M
# Submissions
# 6M
# Acceptance Rate
# 48.6%
# Topics
# Array
# Sorting
# Companies
# 0 - 3 months
# Meta
# 42
# Bloomberg
# 25
# Google
# 22
# Amazon
# 20
# TikTok
# 8
# Microsoft
# 7
# Goldman Sachs
# 3
# Yandex
# 3
# Salesforce
# 3
# Nextdoor
# 3
# 0 - 6 months
# Grammarly
# 10
# Apple
# 8
# Oracle
# 7
# Tesco
# 6
# Atlassian
# 5
# Netflix
# 4
# Zepto
# 4
# Applied Intuition
# 4
# IBM
# 3
# Zoho
# 3
# 6 months ago
# Adobe
# 17
# Yahoo
# 17
# Uber
# 15
# J.P. Morgan
# 13
# LinkedIn
# 12
# Roblox
# 10
# Cisco
# 9
# Justworks
# 7
# Morgan Stanley
# 6
# ServiceNow
# 6
# Similar Questions
# Insert Interval
# Medium
# Meeting Rooms
# Easy
# Meeting Rooms II
# Medium
# Teemo Attacking
# Easy
# Add Bold Tag in String
# Medium
# Range Module
# Hard
# Employee Free Time
# Hard
# Partition Labels
# Medium
# Interval List Intersections
# Medium
# Amount of New Area Painted Each Day
# Hard
# Longest Substring of One Repeating Character
# Hard
# Count Integers in Intervals
# Hard
# Divide Intervals Into Minimum Number of Groups
# Medium
# Determine if Two Events Have Conflict
# Easy
# Count Ways to Group Overlapping Ranges
# Medium
# Points That Intersect With Cars
# Easy
# Count Days Without Meetings
# Medium
# Minimize Connected Groups by Inserting Interval
# Medium
# Discussion (169)