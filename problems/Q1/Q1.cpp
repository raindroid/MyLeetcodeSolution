#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 12ms; 10.5MB
        vector<int> ans;
        unordered_multimap<int, int> nmap;
        
        for (int i = 0; i < nums.size(); i++) {
            nmap.insert({nums[i], i});
        }
        
        for (int i = 0; i < nums.size(); i++) {
            auto found  = nmap.equal_range(target - nums[i]);
            auto it = found.first;
            if (it != found.second && it -> second == i) it++;
            if (it != found.second) {
                ans.push_back(i);
                ans.push_back(it->second);
                return ans;
            }
        }
        return ans;
    }
};

int main() {
    auto nums = vector<int>({2, 7, 11, 15});
    auto res = Solution().twoSum(nums, 9);
    for (auto r : res) {
        cout << r << " ";
    }
    cout << endl;
}