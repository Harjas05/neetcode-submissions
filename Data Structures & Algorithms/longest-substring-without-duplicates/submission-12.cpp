class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> sub;
        if (s.length() == 0) {
            return 0; 
        } 
        if (s.length() == 1) {
            return 1; 
        } 
        int l = 0; 
        int r = 1;
        sub.insert(s[0]); 
        int max = 0; 
        while (r < s.length() && l < s.length()) {
            if (sub.find(s[r]) != sub.end()) {
                if ((r - l) > max) {
                    max = r - l; 
                }
                l++;
                r = l + 1;
                sub.clear();
                sub.insert(s[l]);   
            }
            else {
                sub.insert(s[r]); 
                if (((r - l) + 1) > max) {
                    max = r - l + 1; 
                }
            r++; 
            }
             
        } 
        return max; 
    }
};
