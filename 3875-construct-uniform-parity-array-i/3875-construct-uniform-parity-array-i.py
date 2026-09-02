class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If all numbers have the same parity, keep them as they are.
        if all(x%2==nums1[0]%2 for x in nums1):
            return True
        # If there is at least one odd and one even,
        # every element can be made odd by subtracting
        # an element of the opposite parity.
        return True

"""
Actually, this simplifies to always True under the given constraints.
Why?
If all nums1 values are even → choose every element unchanged → all even.
If all are odd → choose every element unchanged → all odd.
If there are both odd and even:
For an odd x, leave it unchanged → odd.
For an even x, subtract any odd number → even − odd = odd.
Therefore, all elements can be made odd.

So the answer is always True.


return True

"""