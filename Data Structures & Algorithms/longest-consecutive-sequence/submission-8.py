class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numset:
                curr_length = 0
                temp_num = num
                while (temp_num + 1) in numset:
                    curr_length += 1 
                    temp_num += 1
                longest = max(curr_length + 1, longest)
        return longest





        