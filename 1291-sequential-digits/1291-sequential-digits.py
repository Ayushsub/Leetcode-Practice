class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s="123456789"
        ans=[]
        min_len=len(str(low))
        max_len=len(str(high))
        for length in range(min_len,max_len+1):
            for start in range(0,10-length):
                num=int(s[start:start+length])
                if low<=num<=high:
                    ans.append(num)
        return ans

"""
BFS
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        queue = [1,2,3,4,5,6,7,8,9]

        while queue:
            num = queue.pop(0)

            if low <= num <= high:
                ans.append(num)

            last = num % 10
            if last < 9:
                nxt = num * 10 + last + 1
                if nxt <= high:
                    queue.append(nxt)

        return ans
"""