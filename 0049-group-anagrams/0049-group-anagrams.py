class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for word in strs:
            a=''.join(sorted(word))
            
            if a not in s:
                s[a]=[word]
                
            else:
                s[a]+=[word]
                
        return list(s.values())        
