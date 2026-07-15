from collections import Counter

class Solution:
    def minWindow(self,s:str,t:str)->str:
        need=Counter(t)
        left=0
        count=len(t)
        min_len=float('inf')
        start=0
        for right in range(len(s)):
            #if character is needed
            if need[s[right]]>0:
                count-=1
            need[s[right]]-=1
            #valid window found
            while count==0:
                #update minimum window
                if right-left+1<min_len:
                    min_len=right-left+1
                    start=left
                #remove left character
                need[s[left]]+=1
                #window becomes invalid
                if need[s[left]]>0:
                    count+=1
                left+=1

        if min_len==float('inf'):
            return ""

        return s[start:start + min_len]