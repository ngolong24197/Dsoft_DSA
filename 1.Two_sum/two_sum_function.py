class Solution(object):
    
    
    ##Use nested loop
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == complement:
                    return [i,j]
        return []
    
    ##Use dictionary
    def twoSum2(self, nums, target):
        num_to_index = {}
        for i,num in enumerate(nums):
            complement = target - num
            
            if complement in num_to_index:
                return [num_to_index[complement],i]
            
            num_to_index[num] = i
            
        return []
