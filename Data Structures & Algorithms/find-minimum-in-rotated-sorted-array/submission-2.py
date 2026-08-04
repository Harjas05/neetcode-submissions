class Solution:
    def findMin(self, nums: List[int]) -> int:
        # og: 1, 2, 3, 4, 5
        # theres one peak, where the element before is greater thna the element in front
        for i in range(len(nums) - 1):
            if (nums[i]) > nums[i + 1]:
                return nums[i + 1]
        return nums[0]

        