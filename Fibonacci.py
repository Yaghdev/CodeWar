import time

class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.queues = [[ele for ele in que] for que in queues]
        self.capacity = capacity
        try:
            max_height = max(max([cot for cot, que in enumerate(queues) if len(que) > 0]), max([ele for que in queues for ele in que])) 
        except:
            max_height = 0
        self.max_h = max_height
        self.height = len(queues) - 1
        self.direction = 1  # 1 is for Up direction and 0 is for Down
        self.curr_h = 0 # Stating from groud floor
        self.person = []
        self.stops = [0]
    
    def check_person(self):
        for qu in self.queues:
            if len(qu) > 0:
                return True
        return False
                
    def theLift(self):              
        while self.curr_h < self.max_h:             
            person_leave = False
            if len(self.person) > 0:                
                rest_per = []                
                for per in self.person:
                    if per != self.curr_h:
                        rest_per.append(per)  
                    else:
                        person_leave = True                        
                if person_leave:
                    self.stops.append(self.curr_h)                   
                self.person = rest_per 
                
            if len(self.queues[self.curr_h]) > 0:                   
                rest_items = [] 
                is_stop = False
    
                for que in self.queues[self.curr_h]:                    
                    if self.direction and que > self.curr_h:
                        if len(self.person) < self.capacity:
                            is_stop = True
                            self.person.append(que)
                        else:
                            is_stop = True  
                            rest_items.append(que)
                    else:
                        rest_items.append(que)     
                        
                if is_stop and not person_leave and self.stops[len(self.stops)-1] != self.curr_h:
                    self.stops.append(self.curr_h)
                self.queues[self.curr_h] = rest_items 
            self.curr_h += 1
            
        self.direction = 0
        while self.curr_h > 0: 
            person_leave = False            
            if len(self.person) > 0:                
                rest_per = []                
                for per in self.person:
                    if per != self.curr_h:
                        rest_per.append(per)  
                    else:
                        person_leave = True                     
                if person_leave:                    
                    self.stops.append(self.curr_h)                   
                self.person = rest_per 
            
            if len(self.queues[self.curr_h]) > 0:                 
                rest_items = []    
                is_stop = False
                for que in self.queues[self.curr_h]:
                    if not self.direction and que < self.curr_h:                     
                        if len(self.person) < self.capacity:
                            is_stop = True
                            self.person.append(que)
                        else:
                            is_stop = True  
                            rest_items.append(que)
                    else:
                        rest_items.append(que)                 
                if is_stop and not person_leave and self.stops[len(self.stops)-1] != self.curr_h:
                    self.stops.append(self.curr_h)
                self.queues[self.curr_h] = rest_items 
            self.curr_h -= 1 
         
        if self.check_person(): 
            self.direction = 1
            self.theLift()  
            
        if self.stops[len(self.stops)-1] != 0:
            self.stops.append(0)  
            
        return self.stops
    
lift = Dinglemouse(((), (2, 9, 2), (), (8, 6, 10, 1), (13,), (10,), (14,), (4, 0), (4, 2, 10), (1,), (0, 9, 2), (8,), (), (7,), (4, 5, 13, 12)), 1)

lst1 = [0, 1, 2, 3, 4, 5, 6, 8, 10, 14, 13, 11, 10, 9, 8, 7, 4, 3, 1, 3, 4, 5, 6, 9, 14, 13, 11, 10, 9, 8, 7, 5, 1, 2, 3, 4, 5, 6, 14, 13, 11, 10, 9, 8, 7, 4, 3, 4, 5, 10, 14, 12, 11, 10, 9, 8, 7, 4, 5, 13, 10, 9, 8, 7, 0, 5, 10, 9, 8, 7, 1, 10, 8, 7, 2, 8, 7, 2, 7, 0]
lst2 = [0, 1, 2, 3, 4, 5, 6, 8, 10, 14, 13, 11, 10, 9, 8, 7, 4, 3, 1, 3, 4, 5, 6, 9, 14, 13, 11, 10, 9, 8, 7, 5, 1, 2, 3, 4, 5, 6, 14, 13, 11, 10, 9, 8, 7, 4, 3, 4, 5, 10, 14, 12, 11, 10, 9, 8, 7, 4, 5, 13, 10, 9, 8, 7, 0, 5, 10, 10, 9, 8, 7, 1, 10, 8, 7, 2, 8, 7, 2, 7, 0]
print(lift.theLift())
