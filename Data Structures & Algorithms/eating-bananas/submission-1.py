class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles -> num bananas per pile
        # h = hours you have to eat all the bananas
        # upper bound = max(piles)
        # if h > len(piles): we can have a smaller minimum eating rate which would be 
        if h == len(piles):
            return max(piles)
        
        upper_time = max(piles)
        lowest_time = 1
        # 1, 2, 3, 4
        res = 0

        while lowest_time <= upper_time:
            mid = (lowest_time + upper_time) // 2
            print(mid)
            time = 0

            for p in piles:
                time += math.ceil(float(p)/ mid)
            print(time, " time")
            if time > h:
                lowest_time = mid + 1
                print(lowest_time)
            else:
                res = mid
                upper_time = mid - 1
                print(res, upper_time)
        return res



            


        