class Solution {
public:
    bool isPalindrome(string s) {
        
     s.erase(std::remove_if(s.begin(), s.end(), [](char c) { return !std::isalnum(c); }), s.end());
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);

    int begin = 0;
    int end = s.length() - 1;

    if (s.length() <= 1) {
        return true;
    }

    while (begin < end) {
        if (s[begin] != s[end]) {
            return false;
        } else {
            begin++;
            end--;
        }
    }

    return true;
    }
};