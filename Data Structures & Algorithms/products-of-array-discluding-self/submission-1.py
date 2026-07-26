class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force solution 
        # find the product of the entire nums list
        # divide by nums[i] store that result in the output array
        
        # keep track of the products before and after
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        results = [0] * n

        for i in range(1,n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            print(prefix[i], suffix[i])
            results[i] = prefix[i] * suffix[i]
        return results
        


            
