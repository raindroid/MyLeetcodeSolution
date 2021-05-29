class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var charmap = [Character  : Int]()

        var res = 0
        var i = 0

        for (j, char) in s.enumerated() {
            if let chari = charmap[char] {
                i = max(chari, i)
            }
            res = max(res, j - i + 1)
            charmap[char] = j + 1 
        }

        return res
    }
}

print(Solution().lengthOfLongestSubstring(
    "abcabc"
))