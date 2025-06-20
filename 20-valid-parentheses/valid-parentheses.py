class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_char = {")":"(", "}":"{", "]":"["}
        
        for i in s:
            if i in dict_char:
                if stack and dict_char[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False