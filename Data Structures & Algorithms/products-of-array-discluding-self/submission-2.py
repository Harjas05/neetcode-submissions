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

        # for i in range(1,n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i + 1] * nums[i + 1]
        results[0] = 1
        for i in range(1, n):
            results[i] = results[i-1] * nums[i - 1]
        post = 1
        for i in range(n-1, -1, -1):
            results[i] = results[i] * post
            post *= nums[i]

        return results
        


            
