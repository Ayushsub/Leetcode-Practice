class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        for i in range(1,len(strs)):
            j=0
            while j<min(len(a),len(strs[i])) and a[j]==strs[i][j]:
                j+=1
            a=a[:j]

            if a=="":
                return ""

        return a
            
        