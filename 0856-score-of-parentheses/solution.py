class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack =[0] #score of current frame

        for each in s:
            if each == "(":
                # Entering a new, deeper level
                stack.append(0) # The score inside this new parenthesis starts at 0
            else:
                # Found ")" -> close the current level
                inside = stack.pop()  # = the score of everything between this ")" and its matching "(".

                if inside == 0:
                    # Nothing inside -> this is "()", which is worth 1.
                    # Add 1 to the parent frame
                    stack.append(stack.pop() + 1)
                else:
                    # Something with score A was inside -> this is "(A)", worth 2 * A.
                    # Add 2 * A to the parent frame.
                    stack.append(stack.pop() + 2 * inside)

        return stack.pop()
