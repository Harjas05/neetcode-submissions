class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)

        # for stone in stones:
        #     heapq.heappush(max_heap, stone)
        
        x = 0
        y = 0
        while len(stones) != 0 and len(stones) != 1:
            print(x,y)
            y = heapq.heappop_max(stones) 
            x = heapq.heappop_max(stones)
            if y > x:
                c = y - x
                heapq.heappush_max(stones, c)
        
        if len(stones) == 1:
            return stones[0]

        else:
            return 0


        
        