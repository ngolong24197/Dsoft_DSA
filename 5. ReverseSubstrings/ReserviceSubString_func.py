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
    
    ## Use combination of Collections
    def reverseParenthesis2(self,s):
        stack = []
        pairs = {}
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char ==")":
                open_index = stack.pop()
                pairs[open_index] = i
                pairs[i] = open_index
                
        result = []
        i,direction =0,1
        while  0<= i <len(s):
            if s[i] in '()':
                i = pairs[i]
                direction *= -1
            else: 
                result.append(s[i])
            i += direction
            
        print(result)    
        return ''.join(result)
        
      
