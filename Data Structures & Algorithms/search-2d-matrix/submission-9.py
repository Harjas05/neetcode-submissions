class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 
        left = 0
        right = len(matrix) - 1
        # 1 2
        # 3 4
        # 5 6
        # 9 11
        # 12 20

        while left <= right:
            mid = (right + left) // 2
            if (target > matrix[mid][-1]):
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1 
            else:
                break
        if not(left <= right):
            return False
        l = 0
        r = len(matrix[0]) - 1
        # print(left)
        # if left == len(matrix):
        #     left -= 1
            # print(left)
        left = (left + right) // 2
        while l <= r:
            m = (r + l) // 2
            if (target == matrix[left][m]):
                return True
            elif (target > matrix[left][m]):
                l = m + 1
            else:
                r = m - 1 
        return False
        