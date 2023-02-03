class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [0] * n
        result = 0
        for num in nums:
            i,j = 0, result
            while i!=j:
                m = (i+j)//2
                if (tails[m] < num):
                    i = m+1
                else:
                    j = m
            tails[i] = num
            result = max(i+1, result)
        return result
