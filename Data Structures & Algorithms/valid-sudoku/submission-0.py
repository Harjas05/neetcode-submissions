class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # n = 9
        # m = 9
        # row or the col -> 
        # for i in range(9):
        #     filtered = [int(x) for x in board[i] if x.isdigit() and 1 <= int(x) <= 9]
        #     hash_set = set(filtered)
        #     if (len(filtered) != len(hash_set)):
        #         return False
        # for i in range(9):
        #     curr_col = []
        #     for j in range(9):
        #         curr_col.append(board[i][j] if int(board[i][j]).isdigit()  and 1 <= int(board[i][j]) <= 9)
        #     hash_set = set(curr_col)
        #     if (len(curr_col) != len(hash_set)):
        #         return False
        
        start = 0
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] in boxes[(r//3,c//3)]:
                    print("box") 
                    print(r,c,board[r][c])
                    return False

                if board[r][c] in rows[r]:
                    print("row")
                    return False
                if board[r][c] in cols[c]:
                    print("c")
                    return False
                if board[r][c] == ".":
                    continue
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        
        return True


    

        

            
        

        