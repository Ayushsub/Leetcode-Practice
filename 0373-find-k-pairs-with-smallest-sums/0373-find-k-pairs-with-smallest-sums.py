import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap=[]
        #put first pair from nums2 for each nums1 element
        for i in range(min(k,len(nums1))):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        result=[]
        while heap and len(result)<k:
            total,i,j=heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])
            #move to next element in nums2
            if j+1<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))

        return result