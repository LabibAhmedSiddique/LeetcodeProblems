# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                lists[i]=lists[i].next
        arr=sorted(arr)
        if not arr :
            return None
        else:    
            head = ListNode(arr[0])
            current = head

            # Create nodes for the remaining elements and link them
            for item in arr[1:]:
                new_node = ListNode(item)
                current.next = new_node
                current = new_node

        return head    

