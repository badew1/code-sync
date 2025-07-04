class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            if c not in bracket_map:
                stack.append(c)
                continue
            if len(stack) < 1:
                return False
            if stack.pop() != bracket_map[c]:
                return False
        
        if len(stack) != 0:
            return False

        return True