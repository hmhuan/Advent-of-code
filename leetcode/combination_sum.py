# https://leetcode.com/problems/combination-sum

# example: [2,3,6,7] target: 7 -> [[2,2,3],[7]]

# 2 -> 2 -> 
#   -> 3 
# 3 -> 3 -> ..
#    -> 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        def dfs(idx, combination, total):
            if total == target:
                result.append(combination.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            combination.append(candidates[idx])
            dfs(idx, combination, total+candidates[idx])
            combination.pop()
            dfs(idx+1, combination, total)
        
        dfs(0, combination, 0)
        return result
