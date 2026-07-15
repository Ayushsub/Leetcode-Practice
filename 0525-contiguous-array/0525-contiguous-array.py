class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum=0
        max_len=0
        # store first occurrence of prefix sum
        mp = {0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            # prefix sum seen before
            if prefix_sum in mp:
                length=i-mp[prefix_sum]
                max_len=max(max_len,length)
            else:
                mp[prefix_sum]=i

        return max_len
        