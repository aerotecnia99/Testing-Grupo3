from .rule import *
import warnings

class CalledFunctionsNodeVisitor(NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_Attribute(self, node):
        if isinstance(node.value, Call):
            self.functions.append(node.value.func.id)
        
    def total(self):
        return self.functions


class SuperInitNotCalledVisitor(WarningNodeVisitor):
    """Levanta un warning cada vez que en el método init de una subclase no se llame al método __init__ de su super clase"""
    
    def __init__(self):
        super().__init__()
        self.subClass = False

    def visit_ClassDef(self, node: ClassDef):
        if len(node.bases) != 0:
            self.subClass = True
            self.subClassName = node.name
            self.lineno = node.lineno
        NodeVisitor.generic_visit(self, node)
        self.subClass = False
        self.subClassName = None
        self.lineno = None

    def visit_FunctionDef(self, node: FunctionDef):
        if self.subClass and node.name == '__init__':
            visitor = CalledFunctionsNodeVisitor()
            visitor.visit(node)
            called_functions = visitor.total()
            if 'super' not in called_functions:
                self.addWarning('SuperInitNotCalled', self.lineno, 'subclass '+ self.subClassName + ' does not call to super().__init__()')
        

class SuperInitNotCalledRule(Rule):

    def analyze(self, ast):
        visitor = SuperInitNotCalledVisitor()
        visitor.visit(ast)
        return visitor.warningsList()