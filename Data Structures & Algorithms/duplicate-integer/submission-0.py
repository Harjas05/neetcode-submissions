class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_e = set()
        for num in nums:
            if num in unique_e:
                return True
            else:
                unique_e.add(num)
        return False
        