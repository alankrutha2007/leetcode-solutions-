# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root,arr):
            if(root==None):
                return 
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        arr=[]
        inorder(root,arr)
        ans=[]
        max_count=0
        count=1
        for i in range(len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                count+=1
            else:
                count=1
            if(count>max_count):
                max_count=count
                ans=[arr[i]]
            elif(count==max_count):
                if arr[i] not in ans:
                    ans.append(arr[i])
        return ans
