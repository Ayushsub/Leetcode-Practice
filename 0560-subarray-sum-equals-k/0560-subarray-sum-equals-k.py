class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count=0
        #stores:prefix_sum->frequency
        mp={0:1}
        for num in nums:
            prefix_sum+=num
            #check if (prefix_sum-k) exists
            if prefix_sum-k in mp:
                count+=mp[prefix_sum-k]
            #store current prefix sum
            mp[prefix_sum]=mp.get(prefix_sum,0)+1

        return count
        