class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0; 
        int right  = 1;
        int max = 0; 
        unordered_set<char> curr_substr; 
        curr_substr.insert(s[0]); 
        if (s.size() == 0) {
            return 0; 
        } 
        if (s.size() == 1) {
            return 1; 
        }
        while (right < s.size() && left < s.size()) {
            if(curr_substr.find(s[right]) == curr_substr.end()) {
                curr_substr.insert(s[right]);
                if (curr_substr.size() > max) {
                    max = curr_substr.size();
                } 
                right++;  
            }
            else {
                if (curr_substr.size() > max) {
                    max = curr_substr.size();
                } 
                while (curr_substr.find(s[right]) != curr_substr.end()) {
                    curr_substr.erase(s[left]); // only erases if it is present
                        left++;
                }

                    // curr_substr.clear();
                    // bool x = false; 
                    // if (s[left] == s[right]) {
                    //     curr_substr.erase(s[left]); // only erases if it is present
                    //     left++; 
                    // }
                    // if (left == right) {

                    // }
                    // while (s[left] != s[right]) {
                    //     curr_substr.erase(s[left]); // only erases if it is present
                    //     left++;
                    // }
                    // cout << s[left] << " " << s[right]; 
                    // left++;
                    // right = left + 1;  
                    // curr_substr.insert(s[left]); 
                    // if (left == right) {
                    //     right++; 
                    // }
                }
                // check the length of the substring against the max
                // update the leftpointer to be the next valid character that is not the curr character
                // update the right pointer
                // clear the curr_substring
            }
            if (max == 0) {
                return curr_substr.size(); 
            }
            // consider the case where the entire string has no duplicates
        
        return max;
    }
};
