
# Doble herencia
class A:

    def __init__(self, atr_a1, atr_a2, atr_a3):
        self.atr_a1 = atr_a1
        self.atr_a2 = atr_a2
        self.atr_a3 = atr_a3

class B:

    def __init__(self, atr_b1, atr_b2, atr_b3):
        self.atr_a1 = atr_b1
        self.atr_a2 = atr_b2
        self.atr_a3 = atr_b3

class Hija(A,B):

    def __init__(self):
        print("Soy una hija con doble herencia")
        
        


