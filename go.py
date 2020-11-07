import time
class Go:    
    def __init__(self, length=None):
        if length > 25:
            raise Exception("This is invaid")
        self.length = length
        self.turn = 0          # 0 for black and 1 for white
        self.board = [["." for i in range(self.length)] for x in range(self.length)]
   
    def get_position(self, point):
        col = point[-1]
        row = point[0:-1]
        return self.board[self.length - int(row)][int(ord(col))-65]
   
    def get_surrounding(self, point):
        move_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        surrounding = []
       
        for x, y in move_lst:                        
            if(point[0] + x) < self.length and (point[0] + x) >= 0 and (point[1] + y) < self.length and (point[1] + y) >= 0:
                surrounding.append(((point[0] + x), (point[1] + y)))
        return surrounding
   
    def liberties(self, group):      
        liberty = []                  
        for grp in group:
            srr_pnt = self.get_surrounding(grp)
            for sp in srr_pnt:
                if self.board[sp[0]][sp[1]]== '.':
                    if ((sp[0]), (sp[1])) not in liberty:                        
                        liberty.append(((sp[0]), (sp[1])))            
        return liberty
   
    def get_group(self, start_point, pnt_type):
        srr_pnt = self.get_surrounding(start_point)
        print(start_point, srr_pnt, pnt_type)
        group = []
        while srr_pnt:
            pnt = srr_pnt.pop()
            if self.board[pnt[0]][pnt[1]] == pnt_type and pnt not in group: 
                
                group.append(pnt)            
                self.get_group(pnt, pnt_type)          
        return group
   
    def remove_group(self, group):
        for i in group:
             self.board[i[0]][i[1]] = '.'            
        return True
   
    def check_move(self, col, row):
        if self.board[self.length - int(row)][int(ord(col))-65] == 'o' or self.board[self.length - int(row)][int(ord(col))-65] =='x':
            raise Exception("This is invaid")
        else:
            return True            
           
    def move(self, *argv):
        for move in argv:            
            col = move[-1]
            row = move[0:-1]
           
            if self.check_move(col, row):                
                self.board[self.length - int(row)][int(ord(col))-65] = 'o' if self.turn else 'x'                
                pnt_type = 'x' if self.turn else 'o'
                 
                group_lst = self.get_group((self.length - int(row), int(ord(col))-65), pnt_type)  
                print(move, pnt_type, group_lst)
                 
                if len(self.liberties(group_lst)) == 0:
                    self.remove_group(group_lst)
                                   
                self.turn = 0 if self.turn else 1
   

 
game = Go(9)
moves = ["9A","8A","8B","9B"]
game.move(*moves)
print(game.board)
print(game.get_group((0, 0), 'o'))
print(game.get_group((1, 0), 'x'))
print(game.get_group((1, 1), 'o'))
print(game.get_group((0, 1), 'x'))