class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        profit=0
        total_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            elif (price-min_price)>profit:
                profit=price-min_price
                total_profit+=profit
                min_price=price
                profit=0

        return total_profit
    


#     122. Best Time to Buy and Sell Stock II
# Solved
# Medium
# Topics
# Companies
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

# Constraints:

# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 2.3M
# Submissions
# 3.4M
# Acceptance Rate
# 68.5%
# Topics
# Array
# Dynamic Programming
# Greedy
# Companies
# 0 - 3 months
# Amazon
# 13
# Google
# 6
# Meta
# 5
# Bloomberg
# 4
# Microsoft
# 2
# Goldman Sachs
# 2
# Geico
# 2
# 0 - 6 months
# TikTok
# 3
# Apple
# 2
# CTC
# 2
# 6 months ago
# Adobe
# 11
# Uber
# 7
# Citadel
# 6
# Yahoo
# 5
# Zoho
# 4
# Yandex
# 4
# J.P. Morgan
# 3
# tcs
# 3
# Walmart Labs
# 3
# DE Shaw
# 3
# Similar Questions
# Best Time to Buy and Sell Stock
# Easy
# Best Time to Buy and Sell Stock III
# Hard
# Best Time to Buy and Sell Stock IV
# Hard
# Best Time to Buy and Sell Stock with Cooldown
# Medium
# Best Time to Buy and Sell Stock with Transaction Fee
# Medium
# Maximum Profit From Trading Stocks
# Medium
# Discussion (288)