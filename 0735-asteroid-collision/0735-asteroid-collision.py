class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for x in asteroids:
            while st and st[-1]>0 and x<0 and st[-1]<-x:
                st.pop()
            if not st or st[-1]<0 or x>0:
                st.append(x)
            elif st[-1]==-x:
                st.pop()
        return st