class Solution {
public:
    int maxArea(vector<int>& heights) {
      int left = 0; 
      int r = heights.size()-1; 
      int max = 0;
      while (left < r) {
        int width = r - left; 
        int height = min(heights[left], heights[r]); 
        int area = width * height;
        if (area > max) {
            max = area; 
        }
        // int maxh = max(height[left], height[r]);
        if (heights[left] > heights[r]) {
            r--; 
        }
        else if (heights[left] < heights[r]) {
            left++; 
        }  
        else {
            if (heights[left + 1] > heights[r - 1]) {
                left++; 
            }
            else {
                r--; 
            }
        }
      } 
      return max; 
    }
};
