#Description: Given an integer x, return true if x is a palindrome, and false otherwise.
#A palindrome is a number that remains the same when its digits are reversed.

#Input: an integer 
#Output: a boolean value indicating whether the integer is a palindrome

from Palindrome_number_function import Solution

def main():
    solution = Solution()
    
    x1 = 121
    x2 = -121
    x3 = 10
    
    result1 = solution.isPalindrome(x1)
    result2 = solution.isPalindrome(x2)
    result3 = solution.isPalindrome(x3)
    
    print(f"Result1: {result1}")
    print(f"Result2: {result2}")
    print(f"Result3: {result3}")


if __name__ == "__main__":
    main()
