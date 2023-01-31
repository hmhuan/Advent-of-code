# https://leetcode.com/problems/beautiful-arrangement
class Solution:
    def countArrangement(self, n: int) -> int:
        perm = []
        self.result = 0

        def isBeautiful(i, a):
            return i%a==0 or a%i==0
        exists = set()
        m = n+1
        def dfs():
            if len(perm) == n:
                # print(perm)
                self.result += 1
                return
            
            for i in range(1, m):
                if i in exists:
                    continue
                if isBeautiful(len(perm) + 1, i):
                    exists.add(i)
                    perm.append(i)
                    dfs()
                    perm.pop()
                    exists.remove(i)
        dfs()
        return self.result
