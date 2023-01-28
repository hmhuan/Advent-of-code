# https://leetcode.com/problems/generate-parentheses
class Solution:
    combination = ""
    pos = 0
    neg = 0
    def generateParenthesis(self, n: int) -> List[str]:   
        result = []
        targetLen = n * 2
        
        def dfs():
            if (len(self.combination) >= targetLen):
                result.append(self.combination)
                return
            if self.pos < n:
                self.pos += 1
                self.combination += "("
                dfs()
                self.combination = self.combination[:-1]
                self.pos -= 1
            
            if self.neg < self.pos:
                self.neg += 1
                self.combination += ")"
                dfs()
                self.combination = self.combination[:-1]
                self.neg -= 1
            
        dfs()
        return result
