class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sf; 
        unordered_map<char, int> tf;

        for (int i = 0; i < s.length(); i++) {
            sf[s[i]]++; 
        } 
        for (int i = 0; i < t.length(); i++) {
            tf[t[i]]++; 
        } 
        if (s.length() >= t.length()) {
        for (const auto& pair : sf) {
            cout << pair.first << " " << pair.second; 
            if (tf.find(pair.first) == tf.end()) {
                return false; 
            } 
            if (tf[pair.first] != sf[pair.first]) {
                return false; 
            }
        }
        }
        else if (t.length() > s.length()) {
          for (const auto& pair : tf) {
            cout << pair.first << " " << pair.second; 
            if (sf.find(pair.first) == sf.end()) {
                return false; 
            } 
            if (sf[pair.first] != tf[pair.first]) {
                return false; 
            }
        }  
        }
        return true;
    }
};
