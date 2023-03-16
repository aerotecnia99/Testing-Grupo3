# Sintaxis concreta usada para escribir expresiones aritmeticas:
# <expr> = <num>
#        | (+ <expr> <expr>)
#        | (- <expr> <expr>)

class Node:
    # Formatea la expresion en un string
    def to_string(self):
        pass

    # Evalua la expresion
    def eval(self):
        pass

    # Acepta la visita de un visitor
    def accept(self, visitor):
        pass

    # Verifica si un nodo es igual a otro
    def __eq__(self, other):
        return self.__class__ == other.__class__


# Nodos literales normalmente son los valores primitivos (string, entero, boolean)
# En este caso solo consideramos un numero entero
class LiteralNode(Node):
    def __init__(self, val):
        self.value = val

    def to_string(self):
        pass

    def eval(self):
        return self.value

    def accept(self, visitor):
        visitor.visit_Literal(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value


# Numero
class NumberNode(LiteralNode):
    
    def accept(self, visitor):
        visitor.visit_Number(self)

    def to_string(self):
        return "" + str(self.value)


# Operadores
class OperatorNode(Node):
    def __init__(self, sym):
        self.symbol = sym

    def accept(self, visitor):
        visitor.visit_Operator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.symbol == other.symbol


# Operador unario
class UnaryOperatorNode(OperatorNode):
    def __init__(self, onlyNode, sym):
        super().__init__(sym)
        self.onlyNode = onlyNode
    
    def to_string(self):
        return "(" + self.symbol + " " + self.onlyNode.to_string() + ")"

    def accept(self, visitor):
        pass

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.onlyNode == other.onlyNode and self.symbol == other.symbol


# Operador binario
class BinaryOperatorNode(OperatorNode):
    def __init__(self, leftNode, rightNode, sym):
        super().__init__(sym)
        self.leftNode = leftNode
        self.rightNode = rightNode

    def to_string(self):
        return "(" + self.symbol + " " + self.leftNode.to_string() + " " + self.rightNode.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_BinaryOperator(self)
        # Esto al parecer podría ser un pass pq jamás se ocupa directamente esta clase.

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.leftNode == other.leftNode and self.symbol == other.symbol and self.rightNode == other.rightNode


# Operador suma
class AdditionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(AdditionNode, self).__init__(leftNode, rightNode, "+")

    def eval(self):
        return self.leftNode.eval() + self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Addition(self)


# Operador resta
class SubtractionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(SubtractionNode, self).__init__(leftNode, rightNode, "-")

    def eval(self):
        return self.leftNode.eval() - self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Subtract(self)


# Operador Modulo -> Resto :)
class ModuloNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super().__init__(leftNode, rightNode, "%")
        
    def eval(self):
        return self.leftNode.eval() % self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Modulo(self)
        

# Operador PlusPlus
class PlusPlusNode(UnaryOperatorNode):
    def __init__(self, onlyNode):
        super().__init__(onlyNode, "++")
    
    def __eq__(self, other):
        return super().__eq__(other)

    def eval(self):
        return self.onlyNode.eval() + 1

    def to_string(self):
        return super().to_string()

    def accept(self, visitor):
        visitor.visit_PlusPlus(self)

# Operador MinusMinus
class MinusMinusNode(UnaryOperatorNode):
    def __init__(self, onlyNode):
        super().__init__(onlyNode, "--")

    def __eq__(self, other):
        return super().__eq__(other)
    
    def eval(self):
        return self.onlyNode.eval() - 1

    def to_string(self):
        return super().to_string()
    
    def accept(self, visitor):
        visitor.visit_MinusMinus(self)
    

# Visitor
class Visitor:
    # Los nodos compuestos deben propagar la visita a los subnodos
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Subtract(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Modulo(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)
    
    def visit_PlusPlus(self, node):
        node.onlyNode.accept(self)
    
    def visit_MinusMinus(self, node):
        node.onlyNode.accept(self)

    def visit_Number(self, node):
        pass