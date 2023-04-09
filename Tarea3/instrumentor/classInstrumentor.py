from ast import *
import os
from profiler import Profiler


class ClassInstrumentor(NodeTransformer):
    '''inyecta código y recolecta info requerida para el test dinámico a ejecutar'''

    def __init__(self):
        super().__init__()
        self.currentClass = None

    def visit_Module(self, node: Module):
        transformedNode = NodeTransformer.generic_visit(self, node)
        import_profile_injected = parse("from functionInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)
        return transformedNode

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        NodeTransformer.generic_visit(self, node)
        self.currentClass = None

    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        
        # Creación Código a inyectar para llamar a profiler

        if self.currentClass != None:
            # Se inyecta que llama a profiler en la primera linea
            # de la definicón de una función
            argList = list(map(lambda x: x.arg, transformedNode.args.args)) # lista de argumentos de una función
            injectedCode = parse('FunctionProfiler.record(\''+
            transformedNode.name + '\',[' + ", ".join(argList) + '])')
            

            return transformedNode

    # visit method ?


class ClassProfiler(Profiler):

    # Métodos para inyectar código
    @classmethod
    def record(cls, methodName, args):
        cls.getInstance().ins_record(methodName,args)

    # Métodos de instancia
    def __init__(self):
        self.methods_called = []

    def ins_record(self, methodName, args):  
        self.methods_called.append((methodName, args))

    def report_executed_methods(self):
        pass
    
    def report_executed_by(self):
        pass

    

    


def instrument(ast):
    visitor = ClassInstrumentor()
    # devuelve ast con el código inyectado.
    return  fix_missing_locations(visitor.visit(ast))