class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) {
            return false; 
        }
        int l = 0; 
        int r = l + s1.size() - 1;
        vector<int> freqs2(26, 0); 
        vector<int> freqs1(26, 0);

        for (int i = 0; i < s1.size(); i++) {
            freqs1[s1[i] - 'a']++; 
            freqs2[s2[i] - 'a']++; 
        } 

        // unordered_set<char> s1set(s1.begin(), s1.end()); 
        // // string 
        // unordered_set<char> s2set(s2.begin(), s2.end());

        while (r < s2.size() - 1) {
            if (freqs1 == freqs2) {
                return true; 
            }
            else {
                freqs2[s2[l] - 'a']--; 
                l++; 
                r++; 
                freqs2[s2[r] - 'a']++; 
            }
            
            // if (s1set.find(s2[l]) == s1set.end()) {
            //     l++; 
            //     s2set.erase(s2[l]); 
            // }
            // if (s1set.find(s2[r]) == s1set.end()) {
            //     s2set.erase(s2[r]); 
            //     r--; 
            // }
            // if (s1set == s2set) {
            //     return true; 
            // } 
        }
         if (freqs1 == freqs2) {
                return true; 
            }
        return false;

    }
};
