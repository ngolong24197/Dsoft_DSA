class Solution(object):
    
    ##use reverse String method
    def isPalindrome(self, x):
        if (x< 0 or x % 10 == 0 and x != 0):
            return False
        checknum = str(x)
        reversed_checknum = checknum[::-1]
        
        if x == int(reversed_checknum):
            return True
        else:
            return False
      
            
            
    ## use reverse number with operations
    def isPalindrome(self,x):
        if (x< 0 or x % 10 == 0 and x != 0):
            return False
        
        checknum =0
        
        while x > 0:
            checknum = checknum *10 + x % 10
            x //10
            
        return x == checknum 
            
    
    
        
        