from .rewriter import *
import warnings

class MinusEqualsTransformer(NodeTransformer):
    "node visitor subclass"

    # def __init__(self):
    #     super().__init__()
    #     self.currentClass = None

    # def visit_ClassDef(self, node: ClassDef):
    #     self.currentClass = node.name
    #     NodeVisitor.generic_visit(self, node)
    #     self.currentClass = None

    # def visit_Attribute(self, node: Attribute):
    #     if self.currentClass != None:
    #         pass

    def visit_Assign(self, node): #Nodo es "Assign"
        "Retorna el codigo modificado"
        if isinstance(node.value, BinOp): 
            if isinstance(node.value.op, Sub):
                
                # if isinstance(node.targets[0], Attribute):
                #     if node.targets[0].value.id == node.value.left.value.id:
                #         if isinstance(node.value.right, Constant):
                #             # warnings.warn(f'{node.targets[0].id} {node.value.left.id} {node.value.right.value}')
                #             return AugAssign(
                #                 target=Name(id=f'{node.targets[0].value.id}', ctx=Store()),
                #                 op=Sub(),
                #                 value=Constant(value=node.value.right.value)
                #                 )
                #         else: # que sea una variable                   
                #             # warnings.warn(f'{node.targets[0].id} {node.value.left.id} {node.value.right.id}')
                #             return AugAssign(
                #                 target=Name(id=f'{node.targets[0].id}', ctx=Store()),
                #                 op=Sub(),
                #                 value=Name(id=f'{node.value.right.id}', ctx=Load())
                #                 )
                                               
                # else: 
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
