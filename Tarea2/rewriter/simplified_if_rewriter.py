from .rewriter import *
import warnings

class SimplifiedIfTransformer(NodeTransformer):
    "node visitor subclass"

    def visit_IfExp(self, node: IfExp): #Nodo "IfExp"
        "Retorna el codigo modificado"
        
        if isinstance(node.test, Compare): 
            # Caso1: <expression> es True
            if isinstance(node.body, Constant) and node.body.value == True:
                if isinstance(node.orelse, Constant) and node.orelse.value == False:
                    # warnings.warn(f'{node.test} {node.body} {node.orelse}')
                    return node.test
                
            # Caso2: <expresion> es False
            if isinstance(node.body, Constant) and node.body.value == False:
                if isinstance(node.orelse, Constant) and node.orelse.value == True:
                    # warnings.warn(f'{node.test} {node.body} {node.orelse}')
                    return UnaryOp(op=Not(), operand=node.test)
                        #tengo que retornar un nodo Unario
                        # que es la negación de la expresión
                


        

class SimplifiedIfRewriterCommand(RewriterCommand):
    "Transformador de codigo"

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(SimplifiedIfTransformer().visit(ast))
        return new_tree