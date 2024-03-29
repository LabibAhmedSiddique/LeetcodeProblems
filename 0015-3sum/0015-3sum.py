class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        new=[]
        for i , n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sum=n + nums[l] + nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    new.append([nums[l],nums[r],n])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return new            