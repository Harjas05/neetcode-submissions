class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # w = 1
        # h = heights[i]
        # largest rectabgle ( w * h)
        areas = []
        for i in range(len(heights)):
            l = i - 1
            r = i + 1
            w = 1
            while (l >= 0) and heights[l] >= heights[i]:
                w += 1
                l -= 1
            while (r < len(heights)) and heights[r] >= heights[i]:
                w += 1
                r += 1
            areas.append(heights[i] * w)

        return max(areas) 


        