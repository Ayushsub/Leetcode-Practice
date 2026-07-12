class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans=""
        while columnNumber:
            columnNumber-=1
            ans=chr(columnNumber%26+65)+ans
            columnNumber//=26
        return ans
#Adjust by -1 because Excel columns are 1-based.
        
        