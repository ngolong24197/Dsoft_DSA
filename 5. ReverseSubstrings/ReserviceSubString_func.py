class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for character in s:
            if character == ")":
                portion = []
                while stack[-1] != "(":
                    portion.append(stack.pop())
                stack.pop ()
                stack.extend(portion)
            else:
                stack.append(character)
        return "".join(stack)
      
