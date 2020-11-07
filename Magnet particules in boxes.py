def determinant(matrix, total=0):    
    width = len(matrix)
    
    if width == 1:
        return matrix[0][0]    
    if width == 2:        
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]    
    else:
        for i in range(width):
            calc_matix = [[matrix[t][x] for x in range(width) if x != 0] for t in range(width) if t != i]
            sign = (-1) ** (i % 2)           
            temp_sum = determinant(calc_matix)       
            total += sign* matrix[i][0] * temp_sum    
    return total

matrix = [[1, 2, 3, 4], 
          [5, 0, 2, 8], 
          [3, 5, 6, 7], 
          [2, 5, 3, 1]]

print(determinant(matrix))