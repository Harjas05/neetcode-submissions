class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 1) {
            return true;
        }
       string temp = ""; 
       for (int i = 0; i < s.size(); i++) {
        if (isalpha(s[i]) || isdigit(s[i])) {
            temp += tolower(s[i]); 
        }
       }
         
        cout << temp; 
        char* leftptr = &temp[0]; 
        char* rightptr = &temp[temp.size() -1]; 
        while (leftptr <= rightptr) {
            if (*leftptr != *rightptr) {
                return false; 
            }
            leftptr++; 
            rightptr--; 
        }
        return true; 
    }
};
