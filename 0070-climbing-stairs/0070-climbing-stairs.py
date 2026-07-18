class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n<=2:
            return n
        first=1   #ways to reach step 1
        second=2  #ways to reach step 2
        for i in range(3,n+1):
            current=first+second
            first=second
            second=current
        return second


'''Now Reach Step 4 from Step 3

Take ALL ways of step 3:

111
12
21

Now add ONE more step:

111 + 1 = 1111
12 + 1 = 121
21 + 1 = 211

So from step 3,
we got:
3 ways'''