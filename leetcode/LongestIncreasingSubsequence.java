// https://leetcode.com/problems/longest-increasing-subsequence
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int result=0;
        for (int i=0; i<n; ++i){
            dp[i] = 1;
            for (int j=i-1;j>=0;--j){
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}
