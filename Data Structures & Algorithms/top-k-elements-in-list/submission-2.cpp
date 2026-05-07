class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq; 
        for (int i = 0; i < nums.size(); i++) {
            freq[nums[i]]++; 
        }
        // mode -> freq -> 1 = 1; 2 = 2; 3 = 3; 4 = 2
        // vector<pair<int, int>> freqpair; 
        priority_queue<pair<int, int>, vector<pair<int, int>>, less<pair<int, int>>> pq; 
        // elements at top are the ones with highest frequency
        // pq.push({-100000000, -100000}); 
        for (const auto& el:freq) {
            pair<int,int> temp = { el.second, el.first};
            // cout << temp.first << temp.second;  
            pq.push(temp); 
        }
        
        vector<int> fi; 
        for (int i = 0; i < k; i++) {
            fi.push_back(pq.top().second); 
            pq.pop(); 
        }
        return fi; 
        // sort(freqpair.begin(), freqpair.end()); 
        // vector<int> fi; 
        // int j = freqpair.size() - 1; 
        // for (int i = 0; i < k; i++) {
        //     fi.push_back(freqpair[j].second);
        //     j--;  
        // }
        return fi; 

    }
};
