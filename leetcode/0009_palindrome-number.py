class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp=x
        reverse_x=0
        while temp>0:
            last_digit=temp%10
            reverse_x=reverse_x*10+last_digit
            temp=temp//10
        if x==reverse_x:
            return True
        return False