class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        lookup = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for P in s:
            if P in lookup.values():
                stack.append(P)
            elif stack and lookup[P] == stack[-1]:
                stack.pop()
            else:
                return False

        return stack == []
