class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                # we need to check the case of empty stack is firts go like '){}' 
                if not stack or stack.pop() != pairs[ch]:
                    return False
        # also "((((((" cases as we checked at last
        return len(stack) == 0


"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                if not stack or stack.pop() != ch:
                    return False

        return not stack


"""