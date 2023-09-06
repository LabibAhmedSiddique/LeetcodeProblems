class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paranthesis={")": "(", "]": "[", "}": "{"}
        stack=[]
        for i in s:
            if i in paranthesis :
                if stack and stack[-1]== paranthesis[i]:
                    stack.pop()
                else :
                    return False
            else :
                stack.append(i)
        return not stack
        