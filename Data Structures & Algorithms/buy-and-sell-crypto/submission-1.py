class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # int start = 0
        max_m = 0
        min_m = prices[0]
        


        for i in range(len(prices)):

            min_m = min (min_m, prices[i]); 
            # max_ = max(max_, prices[i]); 
            curr_profit = prices[i] - min_m
            max_m = max(max_m, curr_profit)
        return max_m
        
        