class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution 
        # find the product of the entire nums list
        # divide by nums[i] store that result in the output array
        finalprod = 1
        output = []
        zero_count = 0;
        for num in nums:
            if num == 0:
                zero_count += 1 
                if zero_count > 1:
                    return [0] * len(nums)
            else:
                finalprod *= num
        if zero_count == 1:
            for num in nums:
                if num == 0:
                    output.append(finalprod)
                else:
                    output.append(0)
        
        if zero_count == 0:
            for num in nums:
                output.append(finalprod // num)

        
        return output


        