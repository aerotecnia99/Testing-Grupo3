import unittest
from rules import *
from rewriter import *

"""
Template para los tests de las reglas y transformaciones adicionales propuestos por usted.
IMPORTANTE: 
    - Deben existir al menos 5 tests, uno por cada regla/transformador implementado.
    - Los codigos a ser analizados usados en los tests deben ser diferentes.
    - Los tests adicionales deben ser diferentes a los del archivo tests-tarea.py
    - Si usted implemento la tarea en un nuevo archivo dentro del folder rules o rewriter
    no olvide modificar el __init__.py de rules y rewriter para importar los archivos necesarios para su tarea.
    Caso contrario importe lo necesario en este archivo.
"""

class TestWarnings(unittest.TestCase):


    # Funcion que recibe un path del archivo a ser leido y retorna un AST en base al contenido del archivo
    def get_ast_from_file(self, filename):
        file = open(filename)
        fileContent = file.read()
        file.close()
        tree = parse(fileContent)

        return tree

    """ Nombre: test_long_variable_name
        Codigo a ser analizado: extra-test-code/longVariableName.py
        Descripcion: Test para evaluar LongVariableNameRule considerando los siguientes escenarios:
        - Linea 3 : Uso de variable de nombre largo : espantapajaros_del_campo
        - Linea 12 : Uso de variable de instancia, atributo privado, de nombre largo : __kilometraje_recorrido 
        - Linea 16 : Uso de atributo fuera del __init__() de nombre largo: viajar_a_este_lugar
        - Linea 19 : Uso de variable dentro de método de una clase de nombre largo: talleres_de_reparacion_disponibles

        
        Resultado esperado (Una lista de warnings): [
            Warning('VariableLongName', 3, 'variable espantapajaros_del_campo has a long name'),
            Warning('VariableLongName', 12, 'variable __kilometraje_recorrido has a long name'),
            Warning('VariableLongName', 16, 'variable viajar_a_este_lugar has a long name'),
            Warning('VariableLongName', 19, 'variable talleres_de_reparacion_disponibles has a long name'),
        ]
    """

    def test_long_variable_name(self):
        tree = self.get_ast_from_file('extra-test-code/longVariableName.py')

        longNameRule = LongVariableNameRule()
        result = longNameRule.analyze(tree)


        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
            Warning('VariableLongName', 3, 'variable espantapajaros_del_campo has a long name'),
            Warning('VariableLongName', 12, 'variable __kilometraje_recorrido has a long name'),
            Warning('VariableLongName', 16, 'variable viajar_a_este_lugar has a long name'),
            Warning('VariableLongName', 19, 'variable talleres_de_reparacion_disponibles has a long name'),
        ]

        self.assertEqual(result, expectedWarnings)

    """ Nombre: test_unused_argument
        Codigo a ser analizado: extra-test-code/unusedArgument.py
        Descripcion: Test para evaluar UnusedArgumentRule considerando los siguientes escenarios:
        - Linea 2 : En funcion saludar, argumento "saludo" no es usado dentro de la función pero si en su return 
        - Linea 10 : En clase Persona, argumento "rut" no es usado dentro del método __init__(), pero existe atributo de clase tiene el mismo nombre "self.rut" 
        - Linea 19 : En clase Gato, argumento "edad" no es usado dentro del método __init__() pero sí es utilizado dentro de otro método de la clase
        - Linea 32 : En clase Trabajador (subclase de Persona), argumento "empresa" no es usado en super().__init__()
        
        Resultado esperado (Una lista de warnings): [
            Warning('UnusedArgument', 10, 'argument rut is not used'),
            Warning('UnusedArgument', 19, 'argument edad is not used'),
            Warning('UnusedArgument', 32, 'argument empresa is not used')
        ]
    """

    def test_unused_argument(self):
        tree = self.get_ast_from_file('extra-test-code/unusedArgument.py')

        unusedArgRule = UnusedArgumentRule()
        result = unusedArgRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
            Warning('UnusedArgument', 10, 'argument rut is not used'),
            Warning('UnusedArgument', 19, 'argument edad is not used'),
            Warning('UnusedArgument', 32, 'argument empresa is not used')
        ]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_super_init_not_called
        Codigo a ser analizado: extra-test-code/superInitNotCalled.py
        Descripcion: Test para evaluar SuperInitNotCalledRule considerando los siguientes escenarios:
        - Linea 20: Definicion de __init__ de Hija (subclase de A y de B) sin llamada a super().__init__

        Resultado esperado (Una lista de warnings):
            [Warning('SuperInitNotCalled', 17, 'subclass Hija does not call to super().__init__()')]

    """

    def test_super_init_not_called(self):
        tree = self.get_ast_from_file('extra-test-code/superInitNotCalled.py')

        superInitRule = SuperInitNotCalledRule()
        result = superInitRule.analyze(tree)

        # Actualice el valor de expectedWarnings de acuerdo a su caso de prueba propuesto
        expectedWarnings = [
            Warning('SuperInitNotCalled', 17, 'subclass Hija does not call to super().__init__()')
        ]

        self.assertEqual(result, expectedWarnings)


    """ Nombre: test_minus_equal_rewriter
        Codigo a ser analizado: extra-test-code/minusEquals.py
        Descripcion: Test para evaluar transformador MinusEqualsRewriterCommand considerando los siguientes escenarios:
        - Linea 3 : Variable definida en ejecución. Asignación x = x - 7

        
        Resultado esperado: extra-test-code/expectedMinusEquals.py
    """

    def test_minus_equal_rewriter(self):
        tree = self.get_ast_from_file('extra-test-code/minusEquals.py')

        command = MinusEqualsRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedMinusEquals.py')
        #print(unparse(tree))
        self.assertEqual(dump(tree), dump(expectedCode))


    """ Nombre: test_simplified_if
        Codigo a ser analizado: extra-test-code/simplifiedIf.py
        Descripcion: Test para evaluar SimplifiedIfRewriterCommand considerando los siguientes escenarios:
        - Linea 2 : En la construcción de una función lambda. Uso de la expresion if cuando puede ser reemplazada por el if.test
        - Linea 13: En el return de un método dentro de una clase. Uso de la expresion if cuando puede ser reemplazada por el if.test
        
        Resultado esperado: extra-test-code/expectedSimplifiedIf.py
    """

    def test_simplified_if(self):
        tree = self.get_ast_from_file('extra-test-code/simplifiedIf.py')

        command = SimplifiedIfRewriterCommand()
        tree = command.apply(tree)

        expectedCode = self.get_ast_from_file('extra-test-code/expectedSimplifiedIf.py')
        
        self.assertEqual(dump(tree), dump(expectedCode))

if __name__ == '__main__':
    unittest.main()
