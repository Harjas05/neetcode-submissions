class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = {'(', '{', '['}
        mapping = {')': '(', ']': '[', '}': '{'}

        for bracket in s:
            if bracket in opening_brackets:
                stack.append(bracket)
                continue
            if (len(stack) == 0):
                return False
            
            curr = stack[len(stack) - 1]
            stack.pop()
            if (curr != mapping[bracket]):
                return False
        
        return len(stack) == 0