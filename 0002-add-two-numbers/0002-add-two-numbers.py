# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=''
        str2=''
        while l1 :
            str1=str1+str(l1.val)
            l1=l1.next
        while l2 :
            str2=str2+str(l2.val)
            l2=l2.next
        list1=int(str1[::-1])+int(str2[::-1])
           
        list1=list(map(int, str(list1))) 
          
        li=ListNode(list1[0])
        for node in list1[1:]:
            new_node=ListNode(node)
            new_node.next = li
            li= new_node
        return li  
 

            

        