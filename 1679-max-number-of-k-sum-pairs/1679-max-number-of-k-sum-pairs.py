class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d={}
        o=0
        for num in nums:
            if d.get(k-num,0)>0:
                o+=1
                d[k-num]-=1
            else:
                d[num]=d.get(num,0)+1
        return o

        