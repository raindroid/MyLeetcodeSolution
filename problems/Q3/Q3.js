/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const n = s.length
    let charmap = {}

    let res = 0
    let i = 0

    for (const j of Array(n).keys()) {
        i = Math.max(charmap[s[j]] || -1, i)
        res = Math.max(res, j - i + 1)
        charmap[s[j]] = j + 1
    }
    return res
};

console.log(lengthOfLongestSubstring(
    "abcabc"
));