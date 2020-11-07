
def validate(puzzle, x, y, n):
    for i in range(0, 9):
        if puzzle[x][i] == n:
            return False
    
    for i in range(0, 9):
        if puzzle[i][y] == n:
            return False
    
    x0 = x // 3 * 3
    y0 = y // 3 * 3
    
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[i+x0][j+y0] == n:
                return False
    return True
          
def sudoku(puzzle):
    def play(puzzle): 
       
        for i in range(9):
            for j in range(9):            
                if puzzle[i][j] == 0:
                    for n in range(1, 10):
                        if validate(puzzle, i, j, n):
                            puzzle[i][j] = n
                            if play(puzzle):
                                return True
                            puzzle[i][j] = 0
                    return False
        return puzzle
    play(puzzle)         
    return puzzle

 




puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]
 

print(sudoku(puzzle))
