lambda_func = lambda x: x > 10 

class Capibara: 

    def __init__(self, patas):
        self.n_patas = patas

    def tiene_todas_sus_patas(self):
        return self.n_patas == 4