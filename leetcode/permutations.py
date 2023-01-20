class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        used = [False] * len(nums)

        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    perm.append(nums[i])
                    dfs()
                    perm.pop()
                    used[i] = False
        dfs()
        return result
