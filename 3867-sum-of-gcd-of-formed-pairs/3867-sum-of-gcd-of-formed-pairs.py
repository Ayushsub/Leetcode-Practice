from math import gcd
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixgcd=[]
        mx=nums[0]
        for i in range(len(nums)):
            mx=max(nums[i],mx)            
            prefixgcd.append(gcd(nums[i],mx))
        prefixgcd.sort()
        i=0
        j=len(prefixgcd)-1
        ans=0
        while i<j:
            ans+=gcd(prefixgcd[i],prefixgcd[j])
            i+=1
            j-=1
        return ans
            
        