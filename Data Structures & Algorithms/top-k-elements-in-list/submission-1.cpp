class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq; 
        for (int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++; 
        }
        // mode -> freq -> 1 = 1; 2 = 2; 3 = 3; 4 = 2
        vector<pair<int, int>> freqpair; 
        for (const auto& el:freq) {
            pair<int,int> temp = { el.second, el.first}; 
            freqpair.push_back(temp); 

        }
        sort(freqpair.begin(), freqpair.end()); 
        vector<int> fi; 
        int j = freqpair.size() - 1; 
        for (int i = 0; i < k; i++) {
            fi.push_back(freqpair[j].second);
            j--;  
        }
        return fi; 

    }
};
