class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s="".join(sorted(s))
        t="".join(sorted(t))
        for i in range(len(s)):
            if t[i]!=s[i]:
                return t[i]
        return t[-1]
        
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for c in s:
            x ^= ord(c)
        for c in t:
            x ^= ord(c)
        return chr(x)
ord() is a built-in Python function that returns the ASCII (or Unicode) integer value of a character.
"""