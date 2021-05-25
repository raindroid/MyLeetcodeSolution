import java.util.*

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        // 180ms; 36.3MB
        var numMap = hashMapOf<Int, Int>()
        var result = mutableListOf<Int>()

        nums.forEachIndexed { i, k -> run {
            if (target - k in numMap) {
                result.add(numMap.get(target - k) ?: 0)
                result.add(i)
            } else {
                numMap.put(k, i)
            }
        }}

        return result.toIntArray()
    }
}


fun main() {
    println(Arrays.toString(Solution().twoSum(nums = intArrayOf(2,7,11,15), target = 9)))
}