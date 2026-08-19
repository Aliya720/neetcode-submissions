class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        left, right = 0, n-1

        while left < right:
            h = min(heights[left] , heights[right])
            width = right - left
            area = max(area, h * width)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return area        