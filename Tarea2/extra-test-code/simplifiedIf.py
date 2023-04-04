# En la construcción de una función lambda
lambda_func = lambda x: True if x > 10 else False


# En el return de un método en una clase
# Debe levantar warning
class Capibara: 

    def __init__(self, patas):
        self.n_patas = patas

    def tiene_todas_sus_patas(self):
        return True if self.n_patas == 4 else False