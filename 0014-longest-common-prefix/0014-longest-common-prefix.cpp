#include <cmath>
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";

    int prefixLen = 0;
    for (char c : strs[0]) {
        for (int i = 1; i < strs.size(); i++) {
            if (c != strs[i][prefixLen]) {
                return strs[0].substr(0, prefixLen);
            }
        }
        prefixLen++;
    }
    return strs[0].substr(0, prefixLen);
    }
};