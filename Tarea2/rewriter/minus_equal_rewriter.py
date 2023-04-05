from .rewriter import *
# import warnings

# Nota para el ayudante: Esos warnings comentados son de la liberia "warning"
# y los usamos como una forma de obtener info de los errores de otra forma
# pero en estricto rigor no forman parte de nuestra tarea :)

class MinusEqualsTransformer(NodeTransformer):
    "node visitor subclass"

    def visit_Assign(self, node): #Nodo es "Assign"
        "Retorna el codigo modificado"
        if isinstance(node.value, BinOp): 
            if isinstance(node.value.op, Sub):

                if node.targets[0].id == node.value.left.id:
                    if isinstance(node.value.right, Constant):
                        # warnings.warn(f'{node.targets[0].id} {node.value.left.id} {node.value.right.value}')
                        return AugAssign(
                            target=Name(id=f'{node.targets[0].id}', ctx=Store()),
                            op=Sub(),
                            value=Constant(value=node.value.right.value)
                            )
                    else: # que sea una variable                   
                        # warnings.warn(f'{node.targets[0].id} {node.value.left.id} {node.value.right.id}')
                        return AugAssign(
                            target=Name(id=f'{node.targets[0].id}', ctx=Store()),
                            op=Sub(),
                            value=Name(id=f'{node.value.right.id}', ctx=Load())
                            )
                    
        return node #retornar todos los nodos assign a los q si entra pero no tienen una BinOp a la derecha


class MinusEqualsRewriterCommand(RewriterCommand):
    "Transformador de codigo"

    def apply(self, ast):
        # La funcion fix_missing_locations se utiliza para recorrer los nodos del AST y actualizar ciertos atributos (e.g., numero de linea) considerando ahora la modificacion
        new_tree = fix_missing_locations(MinusEqualsTransformer().visit(ast))
        return new_tree
