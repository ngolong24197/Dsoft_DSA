class Solution(object):
    def findLonely1(self, nums):
        result = set()
        not_result = set()
        
        for num in nums:
           
            if (num + 1 in nums) or (num - 1 in nums) or (nums.count(num) > 1):
                not_result.add(num)
            else:
                result.add(num)
        
 
        return list(result)
    
    
    
    
    def findLonely2(self,nums):
        time_appear = {}
        for num in nums:
            time_appear[num] = time_appear.get(num,0)  + 1 ##if no value the default value is 0 
        
        result = []
        for num in time_appear:
            if time_appear[num] == 1 and ( num - 1 not in time_appear) and (num +1 not in time_appear):
                result.append(num) 
        return result
        
