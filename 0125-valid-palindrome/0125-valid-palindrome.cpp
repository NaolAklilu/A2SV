class Solution {
public:
    bool isPalindrome(string s) {
        
    std::string string;
    for (char c : s) {
        if (std::isalnum(c)) {
            string += std::tolower(c);
        }
    }

    int begin = 0;
    int end = string.length() - 1;

    if (string.length() <= 1) {
        return true;
    }

    while (begin < end) {
        if (string[begin] != string[end]) {
            return false;
        } else {
            begin++;
            end--;
        }
    }

    return true;
}
};