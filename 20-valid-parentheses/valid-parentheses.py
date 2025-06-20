class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_char = {")":"(", "}":"{", "]":"["}
        
        for i in s:
            if i in dict_char:
                if stack and dict_char[i] == stack[-1]: # If stack exists and the character is at the stop of the stack and a key
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False