https://leetcode.com/problems/n-queens-ii/description/
class Solution:
    result = 0
    def totalNQueens(self, n: int) -> int:
        posDiag = set()
        negDiag = set()
        col = set()

        def dfs(r):
            if r == n:
                self.result += 1
                return 1
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                dfs(r+1)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                col.remove(c)
        dfs(0)
        return self.result
