
#Description: Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#Input: a string that consists of lower case English letters and brackets.
#Output: a reversed string 

from ReserviceSubString_func import Solution

def main():
    solution = Solution()
    s = "(abcd)"
    
    result1 = solution.reverseParentheses(s)
    
    print(result1)
    
if __name__== "__main__":
    main()
