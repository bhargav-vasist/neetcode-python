class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ("(", "{", "["):
                stack.append(char)
            elif stack and ((char, stack[-1]) in [(')', '(')] or (char, stack[-1]) in [('}', '{')] or (char, stack[-1]) in [(']', '[')]):
                stack.pop()
            else:
                return False
        return not stack


print(Solution().isValid("(){}}{"))
