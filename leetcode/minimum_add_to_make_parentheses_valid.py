# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open, close = 0, 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    close += 1
        return open + close
