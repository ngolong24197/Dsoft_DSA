class Solution(object):
    def isPalindrome(self, x):
        if (x< 0 or x % 10 == 0 and x != 0):
            return False
        checknum = str(x)
        reversed_checknum = checknum[::-1]
        
        if x == int(reversed_checknum):
            return True
        else:
            return False
      
            
            
   
    
    
    
        
        