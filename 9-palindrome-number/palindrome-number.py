class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        arr = x
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = reversed_num * 10 + digit 

        return arr == reversed_num