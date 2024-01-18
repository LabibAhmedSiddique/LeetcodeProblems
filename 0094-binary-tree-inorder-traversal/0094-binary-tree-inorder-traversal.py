# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def inorder(root,li):
            if not root :
                return None
            inorder(root.left,li)
            li.append(root.val)     
            inorder(root.right,li)
            return li   
        inorder(root,li)   
        return li   

        