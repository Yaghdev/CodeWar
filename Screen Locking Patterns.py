import time
def visit_vertex(vertex, dest, visited):
    visit_edges = [(0, 2, 1), (0, 6, 3), (0, 8, 4), (1, 7, 4), (2, 8, 5), (2, 6, 4), (3, 5, 4), (6, 8, 7)]
 
    for i in visit_edges:
        if (vertex == i[0] and dest == i[1]) or (vertex == i[1] and dest == i[0]):
            if i[2] in visited:
                return True
            else:
                return False    
    return True

import copy  
count = 0
def get_visit_node(vertex, length, visited = []):
    global count     
    for x in range(9):
        if vertex != x:           
            if x in visited:
                continue
            
            temp_visited = copy.deepcopy(visited)              
             
            if visit_vertex(vertex, x, temp_visited):                
                temp_visited.append(x)                 
                if len(temp_visited) == length: 
                    count += 1                     
                    continue
                
                get_visit_node(x, length, visited=temp_visited)     
     
def count_patterns_from(firstPoint, length):
    global count
    #start_time = time.time()
    let_to_num = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8}
    visited = []
    if length > 9:
        return 0
    if length == 1:
        return 1    
    count = 0
    visited.append(let_to_num[firstPoint])
    get_visit_node(let_to_num[firstPoint], length, visited)
    #end_time = time.time()
    #print(end_time-start_time)
    return count
        
 
 
   
print(count_patterns_from('C', 4))