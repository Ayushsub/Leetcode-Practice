from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=[0]*10
        for d in digits:
            count[d]+=1
        ans=0
        for h in range(1,10):
            if count[h]==0:
                continue
            count[h]-=1
            for t in range(10):
                if count[t]==0:
                    continue
                count[t]-=1
                for u in range(0,10,2):
                    if count[u]>0:
                        ans+=1
                count[t]+=1
            count[h]+=1
        return ans
