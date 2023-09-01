class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_arr=set(nums)
        longest_streak=0
        
        for vals in new_arr:
            if vals-1 not in new_arr:
                current=vals
                current_streak=1
                while current+1 in new_arr:
                    current+=1
                    current_streak+=1
                longest_streak = max(longest_streak, current_streak)   
        return longest_streak
        