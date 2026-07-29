class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        a=0
        for i in range(len(gain)):
            a=a+gain[i]
            m=max(a,m)
        return m

        