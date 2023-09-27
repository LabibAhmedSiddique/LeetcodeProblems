class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums :
            if n not in freq :
                freq[n]=1
            else :
                freq[n]=freq[n]+1
       
        sorted_dict = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1],reverse=True)}  
        
        arr=list(sorted_dict)[:k]
        return arr