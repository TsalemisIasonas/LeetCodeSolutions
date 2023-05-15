class Solution {
public:
    int strStr(string haystack, string needle) {
        int hSize = haystack.size();
        int nSize = needle.size();
  
        for (int i = 0; i <= hSize - nSize; i++) {
            int j;
            for (j = 0; j < nSize; j++) {
                if (haystack[i + j] != needle[j])
                    break;
            }
        
            if (j == nSize)
                return i;
        }
        return -1;
    }
};