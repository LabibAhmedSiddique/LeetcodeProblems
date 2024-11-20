class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=[]
        b=[]
        for i in set(nums1) :
            if i not in set(nums2):
                a.append(i)
        for j in set(nums2) :
            if j not in set(nums1):
                b.append(j)
        return[a,b]                        

        