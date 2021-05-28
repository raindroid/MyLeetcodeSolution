package problems.Q3;

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        // charmap stores the current index of a character
        var charmap = new HashMap<Character /* use as a char */, Integer>();

        int res = 0;
        int i = 0;

        // try to extend the range [i, j]
        for (int j = 0; j < n; j++) {
            i = Math.max(charmap.getOrDefault(s.charAt(j), -1), i);
            res = Math.max(res, j - i + 1);   // calculate current length
            charmap.put(s.charAt(j), j + 1);
        }
        return res;
    }
}

class Q3 {
    public static void main(String[] args) {
        System.out.println(new Solution().lengthOfLongestSubstring(
            "abcabc"
            ));
    }
}