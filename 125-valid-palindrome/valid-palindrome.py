import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]','',s)
        s=s.lower()
        k=s[::-1]
        if s==k:
            return True
        else:
            return False