from .rule import *

# Nota para el ayudante: Esos warnings comentados son de la liberia "warning"
# y los usamos como una forma de obtener info de los errores de otra forma
# pero en estricto rigor no forman parte de nuestra tarea :)

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
    