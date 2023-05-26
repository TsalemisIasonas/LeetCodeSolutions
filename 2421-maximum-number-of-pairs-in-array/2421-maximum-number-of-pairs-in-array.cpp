class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        vector<bool> removed(n, false);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (!removed[i] && !removed[j] && nums[i] == nums[j]) {
                    count++;
                    removed[i] = true;
                    removed[j] = true;
                    break;
                }
            }
        }
        int left = 0;
        for (int i = 0; i < n; ++i) {
            if (!removed[i]) {
                left++;
            }
        }
        return vector<int>{count, left};
    }
};