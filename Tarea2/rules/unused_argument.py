from .rule import *
import warnings

class ArgNodeVisitor(NodeVisitor):
    def __init__(self):
        self.args = []

    def visit_Name(self, node):
        self.args.append(node.id)
        
    def total(self):
        return self.args


class UnusedArgumentVisitor(WarningNodeVisitor):
    """Se levanta un warning por cada argumento en la definición de un método que no es usado dentro del mismo método"""
    # body = cuerpo de la funcion

    def visit_FunctionDef(self, node: FunctionDef):
        # Si esta definido dentro de un clase, asumir que uno de los argumentos sera self
        visitor = ArgNodeVisitor()
        visitor.visit(node)
        used_arguments = visitor.total()

        for arg in node.args.args: # lista de argumentos q tiene una función "args.args"
            if arg.arg not in used_arguments and arg.arg != 'self': # arg.arg = nombre del argumento
                # warnings.warn(f'UnusedArgument {node.lineno} argument {arg.arg} is not used')
                self.addWarning('UnusedArgument', node.lineno, 'argument '+ arg.arg + ' is not used')
        

class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        return visitor.warningsList()