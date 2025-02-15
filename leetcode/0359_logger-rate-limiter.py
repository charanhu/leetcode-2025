# Method 1
class Logger:

    def __init__(self):
        self.logs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs or timestamp >= self.logs[message]:
            self.logs[message] = timestamp + 10
            return True
        return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# Method 2 (mycode)
class Logger:

    def __init__(self):
        self.current_timestamp = 0
        self.current_message = None
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message and self.current_timestamp == 0:
            self.current_message = message
            self.current_timestamp = timestamp + 10
            self.logs[self.current_message] = self.current_timestamp
            return True
        if message and self.current_message == message:
            if timestamp >= self.logs[message]:
                self.current_message = message
                self.current_timestamp = timestamp + 10
                self.logs[self.current_message] = self.current_timestamp
                return True
            else:
                return False
        if message and self.current_message != message:
            if message not in self.logs:
                self.current_message = message
                self.current_timestamp = timestamp + 10
                self.logs[self.current_message] = self.current_timestamp
                return True
            elif timestamp >= self.logs[message]:
                self.current_message = message
                self.current_timestamp = timestamp + 10
                self.logs[self.current_message] = self.current_timestamp
                return True
            else:
                # self.current_message = message
                # self.current_timestamp = timestamp + 10
                # self.logs[self.current_message] = self.current_timestamp
                return False

        
        


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# 359. Logger Rate Limiter
# Solved
# Easy
# Topics
# Companies
# Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

# All messages will come in chronological order. Several messages may arrive at the same timestamp.

# Implement the Logger class:

# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.
 

# Example 1:

# Input
# ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
# [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
# Output
# [null, true, true, false, false, false, true]

# Explanation
# Logger logger = new Logger();
# logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
# logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
# logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
# logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
# logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
# logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
 

# Constraints:

# 0 <= timestamp <= 109
# Every timestamp will be passed in non-decreasing order (chronological order).
# 1 <= message.length <= 30
# At most 104 calls will be made to shouldPrintMessage.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 350K
# Submissions
# 458.6K
# Acceptance Rate
# 76.3%
# Topics
# Hash Table
# Design
# Data Stream
# Companies
# 0 - 3 months
# Google
# 12
# Netflix
# 2
# Atlassian
# 2
# 0 - 6 months
# Intuit
# 2
# 6 months ago
# Oracle
# 8
# Amazon
# 4
# Bloomberg
# 3
# Microsoft
# 2
# Patreon
# 2
# Grammarly
# 2
# Similar Questions
# Design Hit Counter
# Medium
# Discussion (10)