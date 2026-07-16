class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()
        # -4, -1, -1, 0, 1, 2
        # -2, 0 , 0, 2, 2
        # -2, 0, 1, 1, 2
        

        for i in range(len(nums)):
            start = i + 1
            end = len(nums) - 1
            # goal = 0 - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            

            while (start < end):
                csum = nums[start] + nums[end] + nums[i] 
                if csum < 0:
                    start += 1
                elif csum > 0:
                    end -= 1
                else:
                    res.append( [nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

            
        return res
                
                    

        