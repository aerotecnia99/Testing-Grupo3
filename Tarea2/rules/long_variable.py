from .rule import *


class LongVariableVisitor(WarningNodeVisitor):
    """ Considera variables temporales y de instancia """
    def visit_Attribute(self, node):
        if len(node.attr) > 15:
            self.addWarning("VariableLongName", node.lineno, "variable " + node.attr + " has a long name")
            # warnings.warn(f"VariableLongName {node.lineno} variable {node.attr} has a long name")
        NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        if isinstance(node.ctx, Store):
            if len(node.id) > 15:
                self.addWarning("VariableLongName", node.lineno, "variable " + node.id + " has a long name")
                # warnings.warn(f"VariableLongName {node.lineno} variable {node.id} has a long name")
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