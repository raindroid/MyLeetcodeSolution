class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        val n = s.length
        var charmap = HashMap<Char, Int>()

        var res = 0
        var i = 0

        for (j in 0 .. n - 1) {
            i = Math.max(charmap.getOrDefault(s[j], -1), i)
            res = Math.max(res, j - i + 1)
            charmap.put(s[j], j + 1)
        }

        return res
    }
}

fun main() {
    println(Solution().lengthOfLongestSubstring(
        "abcabc"
    ))
}