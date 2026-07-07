class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        max_len=0
        for right in range(len(s)):
            #remove duplicates from window
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            #add current character
            seen.add(s[right])
            #update maximum length
            max_len = max(max_len,right-left+1)

        return max_len
        