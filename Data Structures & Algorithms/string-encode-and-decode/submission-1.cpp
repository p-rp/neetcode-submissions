class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";

        for (const auto& s: strs)
            encoded += to_string(s.size()) + '#' + s;

        cout << encoded;
        return encoded;
    }

    vector<string> decode(string s) {

        vector<string> arr;
        int i = 0;

        while (i < s.size())
        {
            int j = i;
            while (s[j] != '#')
                j++;
            
            int length = stoi(s.substr(i, j-i));

            i = j+1;
            j = i + length;
            arr.push_back(s.substr(i, length));
            i = j;
        } 

        return arr;
    }
};
