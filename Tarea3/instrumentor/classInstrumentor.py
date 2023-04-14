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
        import_profile_injected = parse("from classInstrumentor import ClassProfiler")
        transformedNode.body.insert(0, import_profile_injected.body[0])
        fix_missing_locations(transformedNode)
        return transformedNode

    def visit_ClassDef(self, node: ClassDef):
        self.currentClass = node.name
        transformedNode = NodeTransformer.generic_visit(self, node)
        self.currentClass = None
        fix_missing_locations(transformedNode)
        return transformedNode

    def visit_FunctionDef(self, node: FunctionDef):
        transformedNode = NodeTransformer.generic_visit(self, node)
        
        # Creación Código a inyectar para llamar a profiler
        if self.currentClass != None:
            injectedCode = parse('ClassProfiler.record(\''+
            transformedNode.name + '\', ' + str(transformedNode.lineno) + ', ' + self.currentClass + ')')
            transformedNode.body.insert(0, injectedCode.body[0])
            
        fix_missing_locations(transformedNode)
        return transformedNode


class ClassProfiler(Profiler):

    # Métodos para inyectar código
    @classmethod
    def record(cls, methodName, lineno, methodClass):
        cls.getInstance().ins_record(methodName, lineno, methodClass)

    # Métodos de instancia
    def __init__(self):
        self.methods_called = set()

    def ins_record(self, methodName, lineno, methodClass):
        self.methods_called.add((methodName, lineno, methodClass.__name__))

    def report_executed_methods(self):
        self.methods_called = sorted(self.methods_called, key=by_lineno)
        print("-- Executed methods --")
        for (fun, lineno, clase) in self.methods_called:
            print(f"Method {fun} called in line {lineno} from class {clase}")
        return self.methods_called
    
    def report_executed_by(self, methodName):
        pass


def instrument(ast):
    visitor = ClassInstrumentor()
    return fix_missing_locations(visitor.visit(ast))


def by_lineno(tuple):
    return tuple[1]
