# https://leetcode.com/problems/symmetric-tree/description/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(l, r):
            if l == None and r == None:
                return True
            if l == None or r == None:
                return False
            if l.val != r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root.left, root.right)
 
