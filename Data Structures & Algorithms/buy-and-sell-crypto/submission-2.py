class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_n = prices[0]; 
        max_p = 0
        for i in range(len(prices)):
            min_n = min(min_n, prices[i])
            curr_p = prices[i] - min_n
            max_p = max(max_p, curr_p )
        return max_p
        