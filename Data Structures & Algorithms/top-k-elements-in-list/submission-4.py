class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1,2,2,3,3,3]
        # k = 2
        # output: array with size k, integers that have the highest frequency

        # hash_map -> frequency 
        # top -k highest freq: keep a list of the highest frequencies
        # priority queue with size k
        hash_map = {}
        # key: num, val freq
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        # prioirty queue:
        # values: pairs <num, freq> sort by frequency
        pq = []

        for x in hash_map:
            heapq.heappush(pq, (hash_map[x], x))
        
        while len(pq) > k:
            heapq.heappop(pq)
        
        results = []
        for pair in pq:
            results.append(pair[1])

        
        return results
        