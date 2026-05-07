class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
       int m = matrix.size(); 
       int n = matrix[0].size();
       // m = 1, n = 1
       int left = 0; 
       int right = m - 1;
       int middle = (left + right) / 2;
       
 
       while ( left <= right) {

            middle = (left + right) / 2;
        if (matrix[middle][0] == target) {
            return true; 
        }
        else if (matrix[middle][0] < target ) {

            if (matrix[middle][n - 1] >= target ) // then the target is in here. 
            {
                for (int i = 0; i < n; i++) {
                    if (matrix[middle][i] == target) {
                        return true;
                    }
                }
                return false; 
            }
            left = middle + 1; 
        }
        else if (matrix[middle][0] > target) {
            right = middle - 1;
        }

        
        
       }
       return false; 
    }
};
