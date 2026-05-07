/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        queue<TreeNode*> q; 
        q.push(root); 
        while (!q.empty()) {
            TreeNode* curr = q.front(); 
            q.pop(); 
            if (isSame(curr, subRoot)) {
                return true; 
            }
            if (curr->left) {
            q.push(curr->left);
            }
            if (curr->right) { 
            q.push(curr->right);
            } 
        }
        return false; 
        // if they are both null
        // if (!subRoot) {
        //     return true; 
        // }
        // if ()
        // bool left; 
        // bool right; 
        // if (root->val == subRoot->val) {
        //     if ((root->left != subRoot->left) || (root->right != subRoot->right)) {
        //         return false; 
        //     }
        //     // bool left = isSubtree(root->left, subRoot->left); 
        //     // bool right = isSubtree(root->right, subRoot->right);
        //     return(isSubtree(root->left, subRoot->left) && isSubtree(root->right, subRoot->right)); 
 
        }
        // return(left && right);
        // return true;  
    
    bool isSame(TreeNode* root, TreeNode* subRoot) {
        if (!root && !subRoot) {
            return true; 
        }
        if (!root || !subRoot) {
            return false; 
        }
        if (root->val != subRoot->val) {
            return false; 
        }
        return (isSame(root->left, subRoot->left) && isSame(root->right, subRoot->right)); 
    }
};
