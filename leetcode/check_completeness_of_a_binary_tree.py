https://leetcode.com/problems/check-completeness-of-a-binary-tree/
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        r = []
        while len(q) > 0:
            n = q.pop(0)
            if n != None:
                r.append(n.val)
                q.append(n.left)
                q.append(n.right)
            else:
                r.append(None)
        for i in range(1, len(r)):
            if r[i-1] == None and r[i] != None:
                return False
        return True
