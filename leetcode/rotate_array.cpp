// https://leetcode.com/problems/rotate-array/submissions/856710935/
class Solution {
public:

    void reverse(vector<int>&nums, int u, int v) {
        int m = v - u;
        for (int i = 0; i < m / 2; ++i) {
            int temp = nums[v - 1 - i];
            nums[v - 1 - i] = nums[u + i];
            nums[u + i] = temp;
        }
    }

    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (k <= 0) {
            return;
        }

        k = k % n;
        reverse(nums, n - k, n);
        reverse(nums, 0, n - k);
        reverse(nums, 0, n);
    }
};
