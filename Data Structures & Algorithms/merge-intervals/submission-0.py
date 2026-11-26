class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorting = sorted(intervals)

        start = sorting[0][0]
        end = sorting[0][1]
        res = []

        for i in range(1, len(intervals)):
            curr_start = sorting[i][0]
            curr_end = sorting[i][1]
            if (curr_start <= end):
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start = curr_start
                end = curr_end
        res.append([start, end])
        return res


            
        