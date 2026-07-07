class Solution:
    def romanToInt(self, s: str) -> int:
        def value(x):
            match x:
                case 'I':
                    return 1
                case 'V':
                    return 5
                case 'X':
                    return 10
                case 'L':
                    return 50
                case 'C':
                    return 100
                case 'D':
                    return 500
                case 'M':
                    return 1000

        def match(a,b):
            if a=='I' and (b=='V' or b=='X'):
                return (value(b)-value(a))
            if a=='X' and (b=='L' or b=='C'):
                return (value(b)-value(a))
            if a=='C' and (b=='D' or b=='M'):
                return (value(b)-value(a))
            else:
                return 0
        
        i = 0
        total = 0
        while i < len(s):
            if i < len(s)-1 and match(s[i], s[i+1]) != 0:
                total += match(s[i], s[i+1])
                i += 2          # Skip both characters
            else:
                total += value(s[i])
                i += 1

        return total


'''
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s)-1 and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total



'''


        
        