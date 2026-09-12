class Solution:
    # def binary_search(self, start: int, end: int, target: int):
    #         while start <= end:    
    #             mi = (start + end) // 2
    #             if (nums[mi] == target):
    #                 return mi
    #             elif target < nums[mi]:
    #                 end = mi - 1
    #             else:
    #                 start = mi + 1
    #         return -1
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        def binary_search(start: int, end: int, target: int):
            while start <= end:    
                mi = (start + end) // 2
                if (nums[mi] == target):
                    return mi
                elif target < nums[mi]:
                    end = mi - 1
                else:
                    start = mi + 1
            return -1
        left = 0
        right = len(nums) - 1
        min_p = -1
        max_p = -1
        pivot = 0

        while left < right:    
            mid = (left + right) // 2
            # if (nums[mid] < )
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left    
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            # temp = nums[0:max_p]
            return binary_search(pivot,len(nums) - 1, target)
        else:
            # last_i = len(nums) - 1
            # temp2 = nums[min_p:last_i + 1]
            # print(min_p, last_i)
            return binary_search(0, pivot - 1, target)
        
