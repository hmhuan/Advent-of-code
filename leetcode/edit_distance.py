# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        result = []
        for i in range(n1+1):
            result.append([0] * (n2+1))
        for i in range(1, n1+1):
            result[i][0] = i
    
        for i in range(1, n2+1):
            result[0][i] = i

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                result[i][j] = result[i-1][j-1]
                if word1[i - 1] != word2[j - 1]:
                    result[i][j] = min(min(result[i - 1][j], result[i][j - 1]), result[i][j]) + 1
    
        return result[n1][n2]
