def spiralize(size):    
    width = size- 1
    hight = size - 1
    maxSize = (size)- 1
    last_item = (0, size - 1)
    direction = 'd'    
    final_array = [[0 for x in range(hight+1)] for i in range(width+1)]
    count = 0 
    for i in range(maxSize+1):
        final_array[0][i] = 1   
    
    while True:        
        if direction == 'r':              
            for i in range(0, maxSize+1):   
                if i < maxSize:
                    final_array[last_item[0]][last_item[1]+1] = 1   
                    last_item = (last_item[0], last_item[1]+1)  
                    if maxSize <=1:                       
                        break
                else:        
                    maxSize = maxSize - 2
                    direction = 'd'
                
        if direction == 'd':
            for i in range(0, maxSize+1):   
                if i < maxSize:                    
                    final_array[last_item[0]+1][last_item[1]] = 1
                    last_item = (last_item[0]+1, last_item[1]) 
                    if maxSize <=1:                        
                        break
                else:
                    direction = 'l'
                    
                
        if direction == 'l':
            for i in range(0, maxSize+1):                
                if i < maxSize:
                    final_array[last_item[0]][last_item[1]-1] = 1   
                    last_item = (last_item[0], last_item[1]-1)
                    if maxSize <=1:                        
                        break
                    
                else:                
                    maxSize = maxSize - 2   
                    direction = 'u'
         
                
        if direction == 'u':                
            for i in range(0, maxSize+1):                  
                if i < maxSize:
                    final_array[last_item[0]-1][last_item[1]] = 1   
                    last_item = (last_item[0]-1, last_item[1])
                    if maxSize <=1:                        
                        break
                    
                else:              
                    direction = 'r'
        
        if maxSize <=1:            
            break
    return final_array
         
                
 

print(spiralize(10))
# print("\n")
# spiralize( [[0,0,0,0,0],
#             [0,0,0,0,1],
#             [1,1,1,0,1],
#             [1,0,0,0,1],
#             [1,1,1,1,1]])
 
[[1,1,1,1,1,1,1,1],
 [0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,0,1],
 [1,0,0,0,0,1,0,1],
 [1,0,1,0,0,1,0,1],
 [1,0,1,1,1,1,0,1],
 [1,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,1,1]]

