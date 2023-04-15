from ast import *
from profiler import Profiler
import inspect


class ClassInstrumentor(NodeTransformer):
    '''inyecta código y recolecta info requerida para el test dinámico a ejecutar'''

    def __init__(self):
        super().__init__()
        self.currentClass = None
        self.currentFunction = None
        self.currentCall = []

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
                transformedNode.name + '\', ' + str(transformedNode.lineno) + ', ' + self.currentClass + ', True)')
            transformedNode.body.insert(0, injectedCode.body[0])
        else:
            self.currentFunction = node.name
            transformedNode = NodeTransformer.generic_visit(self, node)
            injectedCode = parse('ClassProfiler.record(\'' +
                self.currentFunction + '\', ' + str(transformedNode.lineno) + ', ' + '[\'' + "\', \'".join(self.currentCall) + '\']' + ', False, ' + ')')
            self.currentFunction = None
            self.currentCall = []
            transformedNode.body.insert(0, injectedCode.body[0])
        
        fix_missing_locations(transformedNode)
        return transformedNode

    def visit_Call(self, node):
        transformedNode = NodeTransformer.generic_visit(self, node)
        
        if self.currentFunction != None:
            if isinstance(transformedNode.func, Attribute):
                self.currentCall.append(transformedNode.func.attr)
            else:
                self.currentCall.append('__init__')
            
        fix_missing_locations(transformedNode)
        return transformedNode

    def visit_Compare(self, node):
        transformedNode = NodeTransformer.generic_visit(self, node)

        instancias = True
        for element in node.comparators:
            if not isinstance(element, Name):
                instancias = False

        if self.currentFunction != None and instancias:
            self.currentCall.append('__eq__')
            
        fix_missing_locations(transformedNode)
        return transformedNode

class ClassProfiler(Profiler):

    # Métodos para inyectar código
    @classmethod
    def record(cls, methodName, lineno, methodClass, isItMethod):
        if isItMethod:
            cls.getInstance().ins_record(methodName, lineno, methodClass)
        else:
            cls.getInstance().function_record(methodClass, methodName)

    # Métodos de instancia
    def __init__(self):
        self.methods_called = set()
        self.methods_called_by = {}

    def ins_record(self, methodName, lineno, methodClass):
        self.methods_called.add((methodName, lineno, methodClass.__name__))

    def function_record(self, methods, functionName):
        self.methods_called_by[functionName] = set()
        for method in methods:
            for called in self.methods_called:
                if method == called[0]:
                    self.methods_called_by[functionName].add(called)
        self.methods_called_by[functionName] = sorted(self.methods_called_by[functionName], key=by_lineno)
            
    def report_executed_methods(self):
        self.methods_called = sorted(self.methods_called, key=by_lineno)
        print("-- Executed methods --")
        for (fun, lineno, clase) in self.methods_called:
            print(f"Method {fun} called in line {lineno} from class {clase}")
        return self.methods_called
    
    def report_executed_by(self, functionName):
        print(f"-- Executed methods by {functionName} --")
        for (fun, lineno, clase) in self.methods_called_by[functionName]:
            print(f"Method {fun} called in line {lineno} from class {clase}")
        return self.methods_called_by[functionName]


def instrument(ast):
    visitor = ClassInstrumentor()
    return fix_missing_locations(visitor.visit(ast))


def by_lineno(tuple):
    return tuple[1]
