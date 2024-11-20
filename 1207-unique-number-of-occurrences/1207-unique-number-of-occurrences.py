class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt={}
        for n in arr :
            if n not in cnt :
                cnt[n]=1
            else :
                cnt[n]+=1
        nums=list(cnt.values())
        return len(nums) == len(set(nums))            
