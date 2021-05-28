#include <vector>
#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t n = s.size();
        // charmap stores the current index of a character
        unordered_map<char, int> charmap;

        int res = 0;
        int i = 0;

        // try to extend the range [i, j]
        for (int j = 0; j < n; j++) {
            if (charmap.find(s[j]) != charmap.end()) {
                i = max(charmap[s[j]], i); // search for nearest repeated char
            }
            res = max(res, j - i + 1);   // calculate current length
            charmap[s[j]] = j + 1;
        }
        return res;
    }
};

int main() {
    std::cout << Solution().lengthOfLongestSubstring("abcabc") << std::endl;
}