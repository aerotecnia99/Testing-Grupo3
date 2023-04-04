# Argumento no usado dentro de función pero sí en return no debería levantar warning
def saludar(persona, saludo):
    x = "Hola" + persona
    return saludo

# Argumento no usado dentro del método pero un atributo de clase tiene el mismo nombre
# Debe levantar warning
class Persona:

    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = 123456789

# Argumento no usado dentro del método pero sí es utilizado dentro de otro método
# Debe levantar warning
class Gato:

    def __init__(self, nombre, raza, edad, birthday):
        self.nombre = nombre
        self.raza = raza
        self.birthday = birthday

    def edad(self, fecha_actual):
        edad = fecha_actual - self.birthday
        print(edad)

# Argumento no usado en super().__init__()
# Debe levantar warning
class Trabajador(Persona):

    def __init__(self, nombre, apellido, rut, empresa):
        super().__init__(nombre, apellido, rut)

