# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,arr):
            if(root==None):
                return 
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr=[]
        inorder(root,arr)
        newRoot = TreeNode(arr[0])
        curr = newRoot
        for i in range(1, len(arr)):
            curr.right = TreeNode(arr[i])
            curr = curr.right
        return newRoot
