class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> newNums;
        for (int i = 0; i<nums.size()/2; i++){
            newNums.push_back(nums[i]);
            newNums.push_back(nums[i+n]);
        }
        return newNums;
    }
};