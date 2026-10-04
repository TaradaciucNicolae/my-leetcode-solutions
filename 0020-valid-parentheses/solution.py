class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for each in s:
            if each == "(" or each == "[" or each == "{":
                stack.append(each)
                continue

            if not stack:
                return False

            top = stack[-1]

            if each == ")" and top == "(":
                stack.pop()
            
            elif each == "]" and top == "[":
                stack.pop()
            elif each == "}" and top == "{":
                stack.pop()
            else:
                return False

                
        if len(stack) == 0:
            return True
        else:
            return False
