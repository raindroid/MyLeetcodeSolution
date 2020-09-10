class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numDict = [Int: Int] ()
        for (i, k) in nums.enumerated() {
            if let i2 = numDict[target - k] {
                return [i2, i]
            } else {
                numDict[k] = i
            }
        }
        return [0, 1]
    }
}

print(Solution().twoSum([2,7,11,15], 9))
