class TimeMap:

    def __init__(self):
        self.stored = defaultdict(list) # key is string, list of pairs 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp = (value, timestamp)
        self.stored[key].append(temp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stored:
            return ""
        left = 0
        right = len(self.stored[key]) - 1
        target = timestamp
        temp = ""
        last_i = -1
        while (left <= right):
            last_i = left
            mid = (left + right) // 2
            if (self.stored[key][mid][1] == target):
                return self.stored[key][mid][0]
            elif (self.stored[key][mid][1] < target ):
                left = mid + 1
                temp = self.stored[key][mid][0]
            else:
                right = mid - 1

        if self.stored[key][last_i][1] > target and last_i == 0:
            return ""
        # if self.stored[key][last_i][1] < target:
            # return self.stored[key][last_i][0]
        else:
            return temp

            



        
