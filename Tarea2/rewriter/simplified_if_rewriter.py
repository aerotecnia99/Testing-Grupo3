from .rewriter import *

class SimplifiedIfTransformer(NodeTransformer):
    "node visitor subclass"

    def visit_IfExp(self, node): #Nodo "IfExp"
        "Retorna el codigo modificado"
        # if isinstance(node.body,  )
        pass


        

    


class SimplifiedIfRewriterCommand(RewriterCommand):
    "Transformador de codigo"

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree