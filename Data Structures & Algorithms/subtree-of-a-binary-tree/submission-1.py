# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        f = False
        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            right = dfs(p.right, q.right)
            left = dfs(p.left, q.left)

            return right and left
            
        if not root:
            return False
        
        if root.val == subRoot.val:
            f = dfs(root, subRoot)
        
        right = self.isSubtree(root.right, subRoot)
        left = self.isSubtree(root.left, subRoot)

        return right or left or f
