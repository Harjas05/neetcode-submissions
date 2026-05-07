class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       unordered_map<int,int> hmap; 
       for (int i = 0; i < nums.size(); i++) {
        int el = target - nums[i];
        if (hmap.find(el) != hmap.end()) {
            return {hmap[el], i}; 
        }
        hmap[nums[i]] = i;  
       }
    }
};
