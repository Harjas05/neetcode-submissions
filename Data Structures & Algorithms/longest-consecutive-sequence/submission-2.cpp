class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0; 
        }
        if (nums.size() == 1) {
            return 1; 
        }
        unordered_set<int> hash; 
        for (int i = 0; i < nums.size(); i++) {
            hash.insert(nums[i]); 
        }
        int genesis = nums[0]; // implement edge case later if arr is empty
        int max = 0; 
        for (int i = 0; i < nums.size(); i++) {
            if (hash.find(nums[i] + 1) == hash.end()) {
                int ending = nums[i]; 
                int num = 1; 
                while (hash.find(ending - 1) != hash.end()) {
                    ending = ending - 1; 
                    num++; 
                }
                if (num > max) {
                max = num; 
            }

            }

            // bool starting = false; 
            // while (starting != true) {
            //     if (hash.find(genesis -1) != hash.end()) {
            //         genesis = genesis - 1; 
            //         }
            //     else if (hash.find(genesis -1) == hash.end()) {
            //         starting = true; 
            //     }
            // }
            // int num = 0;
            // bool ending = false;  
            // while (ending != true ) {
            //     if (hash.find(genesis + 1) != hash.end()) {
            //         genesis++;
            //         num++;  
            //     }
            //     else {
            //         ending = true; 
            //     }
            // }
            // if (num > max) {
            //     max = num; 
            // }
        }
        return max; 
    }
};
