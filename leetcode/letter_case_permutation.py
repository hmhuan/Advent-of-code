# https://leetcode.com/problems/letter-case-permutation/description/
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        def dfs(idx, ss):
            if idx == n:
                result.append(ss)
                return
            dfs(idx+1, ss+s[idx].lower())
            dfs(idx+1, ss+s[idx].upper())
        dfs(0, "")
        return list(set(result))
