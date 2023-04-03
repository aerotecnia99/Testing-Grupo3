from .rule import *
import warnings


class ArgNodeVisitor(NodeVisitor):
    def __init__(self):
        self.args = []

    def visit_Attribute(self, node: Attribute):
        self.args.append(node.attr)

    def visit_Name(self, node):
        self.args.append(node.id)
        
    def total(self):
        return self.args

class UnusedArgumentVisitor(WarningNodeVisitor):
    """Se levanta un warning por cada argumento en la definición de un método que no es usado dentro del mismo método"""

    def visit_FunctionDef(self, node: FunctionDef):
        # Si esta definido dentro de un clase, asumir que uno de los argumentos sera self
        visitor = ArgNodeVisitor()
        visitor.visit(node)
        argumentos = visitor.total()

        for arg in node.args.args:
            if arg.arg not in argumentos and arg.arg != 'self':
                # warnings.warn(f'UnusedArgument {node.lineno} argument {arg.arg} is not used')
                self.addWarning('UnusedArgument', node.lineno, 'argument '+ arg.arg + ' is not used')
        

class UnusedArgumentRule(Rule):

    def analyze(self, ast):
        visitor = UnusedArgumentVisitor()
        visitor.visit(ast)
        return visitor.warningsList()