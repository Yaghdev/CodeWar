import copy 


def ship_validate(final_list):
    final_lst_copy = copy.deepcopy(final_list)  
    expected_dict = {4:1, 3:2, 2:3, 1:4}
    exp_dict = {}
    while final_lst_copy:
        exp_val = final_lst_copy.pop()
        exp_dict.setdefault(len(exp_val), 0)
        exp_dict[len(exp_val)] += 1
    
    return exp_dict == expected_dict 

def corner_validate(final_list):
    fi_lst = []
    for i in final_list:
        if len(i) > 1:            
            fi_lst.append(i[0]) 
            fi_lst.append(i[len(i)-1])  
        else:
            fi_lst.append(i[0])            
     
    while fi_lst:
        elm = fi_lst.pop()
        elm_1 = (elm[0]+1, elm[1]+1)
        elm_2 = (elm[0]-1, elm[1]+1)
        elm_3 = (elm[0]-1, elm[1]-1)
        elm_4 = (elm[0]+1, elm[1]-1)
        
        if elm_1 in fi_lst or elm_2 in fi_lst or elm_3 in fi_lst or elm_4 in fi_lst:
            return False
    return True
            
                        
        
def validate_battlefield(field):
    temp_dict = {}
    final_list =[]
    track = []
    val_track = []
    tc_id = 0
    
    one_field = [(i, x) for i in range(len(field)) for x in range(len(field)) if field[i][x] ==1]
 
    for i in one_field:     
        if tuple((i[0], i[1]+1)) in one_field and tuple((i[0]+1, i[1])) in one_field:
            return False
        
        if tuple((i[0], i[1]+1)) in one_field:
            cot = 0
            while tuple((i[0], i[1]+cot)) in one_field:
                if tuple((i[0], i[1]+cot)) not in val_track:                    
                    track.append(tuple((i[0], i[1]+cot)))
                    val_track.append(tuple((i[0], i[1]+cot)))
                cot+=1
            if len(track) > 0:
                final_list.append(track)
                track=[]
                         
            
        elif tuple((i[0]+1, i[1])) in one_field:
            cot = 0
            while tuple((i[0]+cot, i[1])) in one_field:
                if tuple((i[0]+cot, i[1])) not in val_track:
                    track.append(tuple((i[0]+cot, i[1])))
                    val_track.append(tuple((i[0]+cot, i[1])))
                cot+=1
            if len(track) > 0:
                final_list.append(track)
                track=[]
            
        else:   
            if tuple((i[0], i[1])) not in val_track:
                final_list.append([i])  
    
 
    if not ship_validate(final_list):
        return False
    
    if not corner_validate(final_list):
        return False
    
    return True


battleField=[[1, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
             [1, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
             [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], 
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
             [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

 

print(validate_battlefield(battleField))