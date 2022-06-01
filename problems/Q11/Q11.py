from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pl = 0
        pr = len(height) - 1
        maxs = min(height[0], height[-1]) * (len(height) - 1)
        while pl < pr and pl < len(height) and pr > 0:
            if (height[pl] < height[pr]):
                pl+=1
            else:
                pr-=1
            maxs = max(maxs, min(height[pl], height[pr]) * (pr - pl))
        
        return maxs
    
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height=height))