# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(root,arr):
            if(root==None):
                return 
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr=[]
        inorder(root,arr)
        total=0
        for num in arr:
            if low<=num<=high:
                total+=num
        return total
