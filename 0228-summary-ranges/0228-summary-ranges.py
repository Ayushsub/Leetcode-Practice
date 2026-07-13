class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans=[]
        c=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if len(c)==1:
                    ans.append(str(c[0]))
                else:
                    ans.append(f"{c[0]}->{c[-1]}")
                c = [nums[i]]
            else:
                c.append(nums[i])
        if len(c)==1:
            ans.append(str(c[0]))
        else:
            ans.append(f"{c[0]}->{c[-1]}")
                
        return ans
        