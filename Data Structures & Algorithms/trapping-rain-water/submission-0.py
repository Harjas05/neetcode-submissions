class Solution:
    def trap(self, height: List[int]) -> int:
        # 0,2,0,3,1,0,1,3,2,1
        # 9

        # 2 pointers 
        # two bars where l < r
        # for all of these indexes in between < height of the smallest bar 
        # area = for each index in between the two bars, height of the smallest bar - height of the bar at the curr index

        max_area = 0

        l = 0
        r = len(height) - 1

        maxleft = height[l]
        maxRight = height[r]

        while (l < r):
            if maxleft < maxRight:
                l += 1
                maxleft = max(maxleft, height[l])
                max_area += maxleft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                max_area += maxRight - height[r]
               


        return max_area


        