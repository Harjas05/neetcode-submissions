class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # w = 1
        # h = heights[i]
        # largest rectabgle ( w * h)
        # areas = []
        # for i in range(len(heights)):
        #     l = i - 1
        #     r = i + 1
        #     w = 1
        #     while (l >= 0) and heights[l] >= heights[i]:
        #         w += 1
        #         l -= 1
        #     while (r < len(heights)) and heights[r] >= heights[i]:
        #         w += 1
        #         r += 1
        #     areas.append(heights[i] * w)

        # return max(areas) 
        maxx = 0

        stack = []

        for i in range(len(heights)):
            # if (stack and heights[i] >= stack[-1]):
            #     stack.append(i, heights[i])
            # if (stack and heights[i] < stack[-1]):
            # elif stack and stack[-1][1] > heights[i]:
                start = i
                while (stack and stack[-1][1] > heights[i]):
                        area = (i - stack[-1][0]) * stack[-1][1]
    # area = (i - stack[-1][0]) * stack[-1][1]
                        maxx = max(area, maxx)
                        start = stack[-1][0]
                        stack.pop()
                stack.append((start, heights[i]))
                    # calculate area
                    # pop
                    # last popped index = starting posiiton and then append
        # if stack:
        while stack:
            l = len(heights)
            areaa = (l - stack[-1][0]) * stack[-1][1]
            maxx = max(areaa, maxx)
            stack.pop()
        



        return maxx



            


        