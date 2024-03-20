class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)
        k=k%a
        nums[:]=nums[a-k:]+nums[:a-k]
        
        