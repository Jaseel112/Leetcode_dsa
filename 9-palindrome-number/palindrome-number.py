class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=str(x)
        if t==t[::-1]:
            return True
        else:
            False