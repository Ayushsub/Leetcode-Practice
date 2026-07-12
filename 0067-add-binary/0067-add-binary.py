class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        while y:
            carry=(x&y)<<1
            x=x^y
            y=carry
        return bin(x)[2:]

#XOR adds bits without carrying, AND finds where a carry should occur
#bin(x) returns '0b10101' The "0b" prefix means it's a binary literal
#int(a,2) means: Convert the string a to an integer, assuming it is written in base 2 (binary)
            



        
        