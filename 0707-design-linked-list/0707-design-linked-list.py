class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)  # Dummy head
        self.right = ListNode(0)  # Dummy tail
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        cur = self.left.next
        for _ in range(index):
            if cur.next is None:  # If we reach the end, index is out of bounds
                return -1
            cur = cur.next
        if cur == self.right:  # If cur points to the dummy tail
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.left, self.left.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if index > 0:  # If index is out of bounds
            return
        node, prev, next = ListNode(val), cur.prev, cur
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        

        cur = self.left.next
        while cur != self.right and index > 0:
            cur = cur.next
            index -= 1
        if cur == self.right or index > 0:  # If index is out of bounds or cur is the dummy tail
            return
        prev, next = cur.prev, cur.next
        prev.next = next
        next.prev = prev
