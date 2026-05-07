class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> freq; 
        // if (nums.size() == 0 ) {
        //     return false;
        // }
        int i = 0; 
        int j = nums.size() - 1; 
        while (i < j) {
            if (freq[nums[i]] > 0) {
                return true; 
            }
            freq[nums[i]]++;
            if (freq[nums[j]] > 0) {
                cout << freq[nums[j]]; 
                return true; 
            }
            // freq[nums[i]]++; 
            freq[nums[j]]++;
            cout << j; 
            cout << freq[2]; 

            i++; 
            j--; 
        }

        return false; 
        
    }
};