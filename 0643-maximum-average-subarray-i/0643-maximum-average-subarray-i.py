class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #first window sum
        window_sum=sum(nums[:k])
        max_sum=window_sum
        #slide the window
        for i in range(k,len(nums)):
            window_sum+=nums[i]-nums[i-k]
            max_sum=max(max_sum,window_sum)

        return max_sum/k
        