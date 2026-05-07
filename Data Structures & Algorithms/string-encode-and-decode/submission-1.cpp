class Solution {
public:

    string encode(vector<string>& strs) {
        string final = ""; 
        for (int i = 0; i < strs.size(); i++) {
            final.append(to_string(strs[i].length())); 
            final += '#'; 
            final.append(strs[i]); 
        }
        // cout << final; 
        return final; 
    }
    //5#stars
    vector<string> decode(string s) {
       vector<string> f; 
    //    cout << s; 
    // cout << s; 
       int i = 0; 
       while (i < s.length()) {
        string currnum = ""; 
        // cout << s; 
        //4#neet4#code4#love3#you
        while(s[i] != '#') {
            currnum += s[i];
            i++;  
        }
        // cout << i; 
        // cout << currnum; 
        // i++; 
        int currnum2 = stoi(currnum);
        // cout << currnum2 << " ";  
        string temp = ""; 
        // cout << i << " "; 
        cout << s[i] << " " << i; 
        for (int j = 0; j < currnum2; j++) {
            // cout << i << " "; 
            temp += s[i + 1];
            // cout << s[i] << " " << i << " "; 
            i++;  
        }
        // cout << i << " ";

        // cout << temp; 
        f.push_back(temp); 
        i++; 
        //currnum = 5
       }
       return f; 
    }
};
