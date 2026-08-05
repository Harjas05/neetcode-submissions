class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        first = -1 
        second = -1
        for i in range(len(nums)):
            diff = target - nums[i]
            # print(diff)
            if diff in hash:
                first = hash[diff]
                second = i
                return [first,second]
            hash[nums[i]] = i
            # print(hash)
        # return [first, second]
        return []


        