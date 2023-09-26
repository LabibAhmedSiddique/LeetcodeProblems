class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check={}
        for i,n in enumerate(nums):
            #check the difference 
            diff=target-n
            #if that difference is in hashmap return the index and i which is the current pointer 
            if diff in check :
                return [check[diff],i]
            #na hole oi index err value and the index it is assigned to will be created in the hashmap    
            check[n]=i    
                
        
                      
        