class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}

        for i, z in enumerate(strs):
            k=''.join(sorted(z))
            if k not in s:
                s[k]=[strs[i]]
            else:
                s[k]+=[strs[i]]   

        
        f=[]
        for vals in s.values():
            f.append(vals)
        return f