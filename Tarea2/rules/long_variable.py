from .rule import *

"""Hi"""

class LongVariableVisitor(WarningNodeVisitor):
    """ Considera variables temporales y de instancia """

    def __init__(self):
        super().__init__()
        self.limit = 15 #mar largo variables

    def visit_Call(self, node):
        if node.func.id == 'eval':
            self.addWarning('EvalWarning', node.lineno, 'eval should not be used!!')
        NodeVisitor.generic_visit(self, node)



class LongVariableNameRule(Rule):

    def analyze(self, ast):
        visitor = LongVariableVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    

##################### BORRRAR ##################


# class Vehiculo():

#     def __init__(self) -> None:
#         self.kilometros = 0

#     def foo(self):
#         print("hola soy vehiculo")

# class Avion(Vehiculo):

#     def __init__(self):
#         # super().__init__()
#         pass
        

# avion = Avion()
# print(avion.foo())

##############################################