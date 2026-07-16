from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        return [num for num, freq in count.most_common(k)]
#Take the elements, sort them by frequency (highest to lowest) and return the first k elements.
    