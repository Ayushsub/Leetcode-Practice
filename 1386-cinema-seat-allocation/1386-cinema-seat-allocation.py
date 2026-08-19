class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        for r,s in reservedSeats:
            d[r]=d.get(r,0)|(1<<s)
        ans=(n-len(d))*2
        for x in d.values():
            a=not(x&(1<<2|1<<3|1<<4|1<<5))
            b=not(x&(1<<4|1<<5|1<<6|1<<7))
            c=not(x&(1<<6|1<<7|1<<8|1<<9))
            ans+=2 if a and c else 1 if a or b or c else 0
        return ans