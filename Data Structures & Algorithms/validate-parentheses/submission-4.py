class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        stack = []

        for c in s:
            if c in ")]}":
                if len(stack) == 0:
                    return False
                elif stack[-1] != brackets[c]:
                    return False
                else:
                    stack.pop()
            elif c in "([{":
                stack.append(c)
            else:
                pass
        return len(stack) == 0
        