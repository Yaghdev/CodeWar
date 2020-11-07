vas_tuple = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 1), (0, -1), (-1, 0), (1, 0)]

def reach_word(n, boardDim):
    reach_array = []
    for i in vas_tuple:
        dim1 = int(n[0])
        dim2 = int(n[1])
        
        if boardDim > int(dim1)+i[0] and int(dim1)+i[0]>=0 and int(dim2)+i[1]>=0 and boardDim > int(dim2)+i[1]:
            reach_array.append((str(int(dim1)+i[0]), str(int(dim2)+i[1])))
    
    return reach_array

def reach_char(ary, char_top, board):
    char_ary = []
    res_ary = []
    
    for i in ary:
        char_ary.append(board[int(i[0])][int(i[1])])
        if board[int(i[0])][int(i[1])] == char_top:
            res_ary.append(i)
       
    return char_ary, res_ary

import copy 
def step_recurs(start_word, req_word, board, path_global=[]):
    path_local = []
    
    char_top = copy.deepcopy(req_word).pop(0)
    reach_state = reach_word(start_word, len(board))
    reach_chars, match_array = reach_char(reach_state, char_top, board)
     
    for i in match_array:
        # print(match_array)
        
        if len(req_word[1:]) > 0:
            path.append(i)
            step_recurs(i, req_word[1:], board, path_global)
       
    print(path)
        
    
    
def find_word(board, word):
    boardDim = len(board)
    
    firstChar = [(str(i), str(x)) for i in range(boardDim) for x in range(boardDim) if word[0] == board[i][x]]
     
    for i in firstChar:
        temp_word = [t for t in word[1:]]
         
        step_recurs(i, temp_word, board)
        
        # print(first_no)
        
        # first_no = i[1]              
        # reach_state = reach_word(first_no, boardDim)
        # reach_chars, match_array = reach_char(reach_state, char_top, board)
        # print(char_top)
        
 
testBoard = [
      ["E","A","R","A"],
      ["N","L","E","C"],
      ["I","A","I","S"],
      ["B","Y","O","R"]
    ]
32
33


find_word(testBoard, "BAILER")
    
     