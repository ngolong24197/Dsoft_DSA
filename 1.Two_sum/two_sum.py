#Description: Given an array of integers nums and an integer target, return index of the two numbers such that they add up to target
#Input: an arrray and a target integer
#Output: the indexes of the two numbers

from two_sum_function import Solution


def main():
    solution = Solution()
    
    nums1 = [2,7,11,15]
    nums2 =[3,2,4]
    nums3 = [3,3]
    
    result1 = solution.twoSum(nums1,9)
    print(f"Result1: {result1} ")
    
    result2 = solution.twoSum(nums2,6)
    print(f"Result1: {result2} ")
    
    
    result3 = solution.twoSum(nums3,6)
    print(f"Result1: {result3} ")
    
if __name__ == "__main__":
    main()
