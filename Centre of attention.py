

class Central_Pixels_Finder(object):
    def __init__(self, data, w, h): 
        self.pixels = data
        self.width = w
        self.height = h    
    
    def next_move(self, position, direction):
        if direction =='up':
            if (position[0] - 1) >= 0:
                return ((position[0]-1), position[1])
            else:
                return ((self.height-1), position[1])
        
        if direction =='right':
            if (position[1] + 1) <= self.width-1:
                return (position[0], position[1] + 1)
            else:
                return (position[0], 0)  
            
        if direction =='down':
            if (position[0] + 1) <= self.height-1:
                return ((position[0] + 1), position[1])
            else:
                return (0, position[1])
            
        if direction =='left':
            if (position[1] - 1) >= 0:
                return ((position[0]), (position[1]-1))
            else:
                return (position[0], (self.width-1))
        
    
    def recursive_fun(self, start_point):
        # up 
        visited = []
        if self.next_move(start_point, 'up') in self.color_list:
            visited.append(start_point)
            if 
            recursive_fun()
        
        
            
         
           
    def central_pixels(self, colour):
        direction_lst = [(0, 1), (1, 0), (-1, 0), (0, -1)]   # right, down, up, left
        
        color_list = [(row, count) for row in range(self.height) for count, i in enumerate(self.pixels[row*self.width:(row+1)*self.width]) if i== colour]    
        org_matrix = [ [i for count, i in enumerate(self.pixels[row*self.width:(row+1)*self.width])] for row in range(self.height)]     
        
        self.color_list = color_list
        self.org_matrix = org_matrix
        #self.recursive_fun()
        
         
image = Central_Pixels_Finder( [1,1,4,4,4,4,2,2,2,2,
                                1,1,1,1,2,2,2,2,2,2,
                                1,1,1,1,2,2,2,2,2,2,
                                1,1,1,1,1,3,2,2,2,2,
                                1,1,1,1,1,3,3,3,2,2,
                                1,1,1,1,1,1,3,3,3,3], 10, 6 );

# image.central_pixels(1)
print(image.central_pixels((1)))