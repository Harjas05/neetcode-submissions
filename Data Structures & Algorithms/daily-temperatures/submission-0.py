class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # store the pairs of the index and then the actual temeprature



        n = (len(temperatures)) 
        # when we reach three, pop from the stack until the top element is >= of stakc is  curr element 
        for i, t in enumerate(temperatures):
            while(stack and t > stack[-1][0]):
                temp, index = stack.pop()
                diff = i - index
                result[index] = diff
            stack.append([t,i])
        return result





        