package problems.Q1;

import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // 1ms; 39.9MB
        HashMap<Integer, Integer> numMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int k = nums[i];
            if (numMap.containsKey(target - k)) {
                return new int[] {numMap.get(target - k), i};
            } else {
                numMap.put(k, i);
            }
        }
        return new int[]{0, 1};
    }

}

class Q1 {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Solution().twoSum(new int[]{2, 7, 11, 15}, 9)));
    }
}
