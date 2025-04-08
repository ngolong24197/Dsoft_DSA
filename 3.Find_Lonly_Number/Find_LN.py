#Description: Given an integer array nums, return all the lonely numbers in the array. 
# A lonely number is a number that appears exactly once in the array and does not have any adjacent numbers (i.e., its value minus 1 and its value plus 1) in the array.
#Input: an integer array nums
#Ouput: an integer array of lonely numbers

from Find_LN_Func import *

def main():
    
    solution = Solution()
    
    nums = [10,6,5,8]
    result = solution.findLonely2(nums)
    print(result)


if __name__ == "__main__":
    main()
