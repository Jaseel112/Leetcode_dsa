class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s)
        e=[x for x in c.values() if x%2==0]
        o=[x for x in c.values() if x%2!=0]
        if o:
            odd=sum(o)-(len(o)-1)
            return sum(e)+odd
        else:
            return sum(e) 
