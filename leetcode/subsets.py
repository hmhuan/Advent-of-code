# https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        subset = []
        chosen = [False] * n
        def dfs(idx):
            result.append(subset.copy())
            for i in range(idx, n):
                if chosen[i]:
                    continue
                chosen[i] = True
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                chosen[i] = False
        dfs(0)
        return result
