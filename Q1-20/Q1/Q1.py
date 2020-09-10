from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        52ms; 15.2MB
        >>> Solution().twoSum(nums = [2,7,11,15], target = 9)
        [0, 1]
        """
        num_dict = {}
        for i, k in enumerate(nums):
            if target - k in num_dict:
                return [num_dict[target - k], i]
            else:
                num_dict[k] = i



print(Solution().twoSum(nums = [2,7,11,15], target = 9))