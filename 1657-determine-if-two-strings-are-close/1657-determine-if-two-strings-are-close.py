
class Solution:
          

    def closeStrings(self, word1: str, word2: str) -> bool:
        def counter(word):
            s={}
            for n in word :
                if not n in s :
                    s[n]=1
                else :
                    s[n]+=1
            return s          
        if len(word1)!=len(word2):
            return False
        return (counter(word1).keys()==counter(word2).keys()) and (sorted(counter(word1).values()) ==sorted(counter(word2).values()))
        