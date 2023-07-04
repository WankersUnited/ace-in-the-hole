class CardCounter:
    def __init__(self):
        self._count = 0
        self._cards_left = {
            '2c' : 1, '2d' : 1, '2h' : 1, '2s' : 1, 
            '3c' : 1, '3d' : 1, '3h' : 1, '3s' : 1, 
            '4c' : 1, '4d' : 1, '4h' : 1, '4s' : 1, 
            '5c' : 1, '5d' : 1, '5h' : 1, '5s' : 1, 
            '6c' : 1, '6d' : 1, '6h' : 1, '6s' : 1, 
            '7c' : 0, '7d' : 0, '7h' : 0, '7s' : 0, 
            '8c' : 0, '8d' : 0, '8h' : 0, '8s' : 0, 
            '9c' : 0, '9d' : 0, '9h' : 0, '9s' : 0, 
            '10c' : -1, '10d' : -1, '10h' : -1, '10s' : -1,
            'Ac' : -1, 'Ad' : -1, 'Ah' : -1, 'As' : -1, 
            'Jc' : -1, 'Jd' : -1, 'Jh' : -1, 'Js' : -1, 
            'Kc' : -1, 'Kd' : -1, 'Kh' : -1, 'Ks' : -1, 
            'Qc' : -1, 'Qd' : -1, 'Qh' : -1, 'Qs' : -1
        }
        
    def see(self, ):
        # Values seen passed in from ml model
        # Checked if appeared before
        # if not appeard, return card and remove entry from _cards
        return
    
    def count(self, x):
        hash
        self._count += 0
        return
    
    def choose_strategy(self):
        if self._count:
            return
        return