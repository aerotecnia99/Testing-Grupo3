# variables definidas en ejecucion
x = 4
x = x - 7

# variable definida en un metodo de una función
class Alcancia:

    def __init__(self, color, n_monedas):
        self.color = color
        self.n_monedas = n_monedas

    def pagos_del_mes(self):
        self.n_monedas = self.n_monedas - 100 

