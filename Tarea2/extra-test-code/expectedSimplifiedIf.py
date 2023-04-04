# En la construcción de una función lambda
lambda_func = lambda x: x > 10 


# En el return de un método en una clase
# Debe levantar warning
class Capibara: 

    def __init__(self, patas):
        self.n_patas = patas

    def tiene_todas_sus_patas(self):
        return self.n_patas == 4 