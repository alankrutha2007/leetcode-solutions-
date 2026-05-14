# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root,arr):
            if(root==None):
                return 
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr=[]
        inorder(root,arr)
        left,right=0,len(arr)-1
        while(left<right):
            sum=arr[left]+arr[right]
            if(sum==k):
                return True
            elif(sum<k):
                left+=1
            elif(sum>k):
                right-=1
        return False 
