# https://leetcode.com/problems/letter-case-permutation/description/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = set()
        chars = []
        n = len(s)
        def dfs(idx):
            if len(chars) == n:
                result.add(''.join(chars))
            for i in range(idx, n):
                chars.append(s[i].lower())
                dfs(i+1)
                chars.pop()
                
                chars.append(s[i].upper())
                dfs(i+1)
                chars.pop()
        dfs(0)
        return result
