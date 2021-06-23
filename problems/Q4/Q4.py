from typing import List

class Solution: # Binary search
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0 or len(nums2) == 0:
            nums = nums1 + nums2
            half = (len(nums) - 1) // 2
            odd = len(nums) % 2
            if odd:
                return nums[half]
            else:
                return (nums[half] + nums[half + 1]) / 2


        nums1 = [-10**7] + nums1 + [10**7]
        nums2 = [-10**7] + nums2 + [10**7]
        
        half = (len(nums1) + len(nums2)) // 2
        odd = (len(nums1) + len(nums2)) % 2
        print(half, odd)
        left1, right1 = 0, len(nums1) - 1
        i = 0
        while True and i < 10:
            i += 1
            print(f"i={i}")
            left1, right1, middle1, size1 = self.binSearch(left1, right1)
            middle2 = half - middle1 - 2
        
            print(middle1, middle2)
            print(nums1[middle1], nums2[middle2])
            if nums1[middle1] > nums2[middle2 + 1]:
                right1 = middle1 - 1
            elif nums2[middle2] > nums1[middle1 + 1]:
                left1 = middle1 + 1
            else:
                break
            print(left1, right1)
        
        large_median = min(nums1[middle1 + 1], nums2[middle2 + 1])
        small_median = max(nums1[middle1], nums2[middle2])
        if odd:
            return large_median
        else:
            return (large_median + small_median) / 2.0      

    def binSearch(self, left, right) -> (int, int, int, int):
        middle = (left + right) // 2
        return left, right, middle, middle + 1


class Solution2: # find kth number by removing the others half by half
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n // 2 + 1)
        else:
            small = self.findKth(nums1, nums2, n // 2)
            big = self.findKth(nums1, nums2, n // 2 + 1)
            return (small + big) / 2.0

    def findKth(self, a, b, k):
        if len(a) == 0:
            return b[k - 1]

        if len(b) == 0:
            return a[k - 1]

        if k == 1:
            return min(a[0], b[0])

        nb = b[k // 2 - 1] if len(b) >= k // 2 else None
        na = a[k // 2 - 1] if len(a) >= k // 2 else None

        if nb is None or (na is not None and na < nb):
            return self.findKth(a[k // 2:], b, k - k // 2)
        else:
            return self.findKth(a, b[k//2:], k - k // 2)

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays(
        [1],
        []
    ))