class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        for x in candies:
            if x+extraCandies>=max(candies):
                a.append(bool(1))
            else:
                a.append(bool(0))
        return a
        