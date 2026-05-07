class KthLargest {
public:
    // vector<int> stream;
    // max pq 
    priority_queue<int, vector<int>, std::greater<int>> stream; 
    int realK = -1;  
    // vector<int> numss;
    KthLargest(int k, vector<int>& nums)  {
        realK = k; 
        // numss = nums; 
        for (int i = 0; i < nums.size(); i++) {
            // cout << nums[i]; 
            stream.push(nums[i]); 
        }
        while (stream.size() > realK) {
            stream.pop(); 
        }
        // cout << stream.size(); 
        //ctor - inpace
        // for (int i = 0 ; i < stream.size(); i++) {
        //     cout << stream.top(); 
        //     stream.pop(); 
        // }
    }
    // 8,7,6,5,3.3,3,, 2, 1
    // priority heap min or max??
    int add(int val) {
        stream.push(val);
        if (stream.size() > realK) {
            stream.pop(); 
        }
        return stream.top(); 
      
    }
};
