import time
class Hand:    
    def __init__(self, cards_lst):
        self.cards_lst = cards_lst
        self.card_type = {"♣":0, "♠":1, "♦":2, "♥":3}
        self.score = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13}
        
    def get_hand(self):
        pass
    
    def sort_sequence(self, card_lst):
        is_sorting_complete = False
        while is_sorting_complete == False:
            is_sorting_complete = True
            for i in range(0, len(card_lst)-1):
                if int(self.card_type[card_lst[i][1]]) +self.score[str(card_lst[i][0])]  > int(self.card_type[card_lst[i][1]]) + self.score[str(card_lst[i+1][0])]:
                    a = card_lst[i+1]
                    card_lst[i+1] = card_lst[i]
                    card_lst[i] = a
                    is_sorting_complete = False
        
        return card_lst[::-1]
    
    def combine_cards(self, card_lst):
        for i in card_lst:
            if i[1] == 
        
                    
    
    def get_runs(self):
        sort_cards = self.sort_sequence(self.cards_lst)
     
        step_pairs = []
        common_pairs = []
    
        step_pair_set = set()
        common_pair_set = set()
        print(sort_cards)
        for i in range(0, len(sort_cards)-1):
            # find step pairs in the cards
            if self.score[sort_cards[i][0]] - 1 == self.score[sort_cards[i+1][0]] and sort_cards[i][1] == sort_cards[i+1][1]:
                step_pair_set.add(sort_cards[i])
                step_pair_set.add(sort_cards[i+1])
            else:
                if len(step_pair_set) >= 3:
                    step_pairs.append(sorted(list(step_pair_set), key=lambda step: int(self.score[step[0]])))
                step_pair_set = set()
            
            
            if i == len(sort_cards)-2:
                if len(step_pair_set) >= 3:
                    step_pairs.append(sorted(list(step_pair_set), key=lambda step: int(self.score[step[0]])))
                step_pair_set = set()
            
#            if self.score[sort_cards[i][0]] == self.score[sort_cards[i+1][0]] and sort_cards[i][1] != sort_cards[i+1][1]:
#                common_pair_set.add(sort_cards[i])
#                common_pair_set.add(sort_cards[i+1])
#                if len(step_pair_set) >= 3:
#                    common_pairs.append(list(step_pair_set)[::-1])
#                    common_pairs = set()
                
                 
        
        print(step_pairs)
                
            
            
            
                        
    
    def get_sets(self):
        res_dict = {}
        for i in self.cards_lst:
            res_dict.setdefault(i[0], [])
            res_dict[i[0]].append(i)
        return [i for i in res_dict.values() if len(i) >= 3]
    
    
    def get_score(self):
        print(self.get_runs())                
    
    def add_card(self,c):
        pass


BASIC_TESTS = [
    ("Single Set: Get Score",     '3♠ 3♦ 3♥ 4♥ 8♦ J♠ K♠', 36),
    ("Single Runs: Get Score",    '7♦ 6♦ 8♦ A♣ 2♥ 5♥ 6♠', 14),
    ("Two Melds: Get Score",      '5♠ 5♦ 5♥ 7♥ 8♥ 9♥ 2♥', 2),
    ("Multiple Melds: Get Score", 'A♠ 2♠ 3♠ 3♦ 3♥ 4♠ 5♠', 6),
]
    

hand = Hand("A♠ 2♠ 3♠ 4♠ 3♦ 3♥ 4♠ 5♠".split())

print(hand.get_score())

