class Solution {
public:
    int maxProfit(vector<int>& prices) {
    //    unordered_set<int> prev; 
    //    prev.insert(prices[0]); 
    //    int maxprof = - 10000; 
    //    for (int i = 1; i < nums.size(); i++) {

    //    }  
    int max = -1000; 
    for (int i = 0; i < prices.size(); i++) {
        for (int j = i + 1; j < prices.size(); j++) {
            int currprof = prices[j] - prices[i]; 
            if (currprof > max) {
                max = currprof; 
            }
        }     
    }
    if (max <= 0) {
        return 0; 
    }
    else {
        return max; 
    }
    }
};
