class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> x; 
        for (int i = 0; i < strs.size(); i++) {
            string curr = strs[i]; 
            sort(curr.begin(), curr.end()); 
            x[curr].push_back(strs[i]); 
        }
        vector<vector<string>> final; 
        for (const auto& el: x) {
            final.push_back(el.second); 
        }
        return final; 

    }
};
