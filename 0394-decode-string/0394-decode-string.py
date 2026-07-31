class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch!=']':
                st.append(ch)
            else:
                temp=""
                while st[-1]!='[':
                    temp=st.pop()+temp
                st.pop()
                num=""
                while st and st[-1].isdigit():  #st[-1] in "0123456789"
                    num=st.pop()+num
                st.append(temp*int(num))
        return "".join(st)