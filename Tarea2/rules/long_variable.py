from .rule import *


class LongVariableVisitor(WarningNodeVisitor):
    """ Considera variables temporales y de instancia """

    def visit_Assign(self, node: Assign):
        
        # if len(node.id) > 15: # and node.ctx == Store()
        #     self.addWarning('VariableLongName', node.lineno, 'variable' + node.id + 'has a long name')
        # NodeVisitor.generic_visit(self, node)

        # if isinstance(node, Assign):
        #     targets = node.targets
        # else:
        #     targets = node.args + node.body
            for target in targets:
                if isinstance(target, Name):
                    # if isinstance(target, ast.Attribute):
                    #     continue
                    if len(target.id) > 15:
                        self.addWarning("VariableLongName", target.lineno,
                                        "variable " + target.id + " has a long name")
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