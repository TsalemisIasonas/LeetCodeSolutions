class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int max = candies[0];
        for (int i: candies){
            if (i>max){
                max = i;
            }
        }
        for (int i: candies){
            if (i+extraCandies >= max){
                result.push_back(true);
            }
            else result.push_back(false);
        }
        return result;
    }
};