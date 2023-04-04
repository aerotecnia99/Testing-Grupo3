# Variable definida en ejecución
saludo = 'hola'
espantapajaros_del_campo = []


class Auto:

    def __init__(self, marca, estado, km, bencina):
        self.marca = marca
        self.estado = estado
        self.bencina = bencina
        self.__kilometraje_recorrido = km               # Caso atributo privado

    def viajar(self, origen, destino):
        self.origen = origen
        self.viajar_a_este_lugar = destino              # Caso atributo definido fuera del init

    def reparar(self, talleres):
        talleres_de_reparacion_disponibles = talleres   # Variable dentro de clase
