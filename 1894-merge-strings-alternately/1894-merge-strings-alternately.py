class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strq=''
        minres=min(len(word1),len(word2))
        for i in range(minres):
            strq+=word1[i]
            strq+=word2[i]
        if len(word1)<len(word2):
            strq=strq+word2[len(word1):]  
        else:
            strq=strq+word1[len(word2):]    
        return strq    