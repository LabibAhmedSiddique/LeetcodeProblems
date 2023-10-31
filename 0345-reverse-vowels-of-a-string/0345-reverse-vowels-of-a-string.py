class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        
        vowels=set('AEIOUaeiou')
        new=list(s)
        r=len(new)-1
        while l<r:
            while l<r and new[l] not in vowels:
                l+=1
            while l<r and new[r] not in vowels :
                r-=1
            
            new[l],new[r]=new[r],new[l]
            l+=1
            r-=1
        return ''.join(new)            

        