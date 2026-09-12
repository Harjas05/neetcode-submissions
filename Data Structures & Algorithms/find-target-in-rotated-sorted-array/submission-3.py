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
        def binary_search(start: int, end: int):
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
        pivot = 0

        while left < right:    
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left    
        if target >= nums[pivot] and target <= nums[len(nums) - 1]:
            return binary_search(pivot,len(nums) - 1)
        else:
            return binary_search(0, pivot - 1)
        
