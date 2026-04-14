class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                my_stack.append(s[i])
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(my_stack) != 0:
                    if my_stack[-1] + s[i]== "[]" or my_stack[-1] + s[i] == "()" or my_stack[-1] + s[i] == "{}":
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(my_stack) == 0:
            return True
        else:
            return False
