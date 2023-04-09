import sys
import inspect
from types import *
import traceback
from stackInspector import StackInspector

""" Clase para rastrear que partes de codigo se ejecutan.
Use de la siguiente forma: with Tracer(): block() """
class Tracer(StackInspector):

	# Inicializa las variables para rastrear un bloque de codigo y mandar logs a 'file'
    def __init__(self, *, file = sys.stdout):
        super().__init__(None, self.traceit)
        self.file = file

    """Funcion de rastreo que llama a imprimir los eventos y evita que rastreemos nuestros propios metodos
    Por el momento esta funcion envuelve a:
    - Un evento (event): Es una cadena que puede tener los siguientes valores:
    	* 'line' 	- una nueva linea siendo ejecutada
    	* 'call' 	- una funcion que acaba de ser llamada
    	* 'return' 	- el retorno de una funcion
    - Un frame: El frame de ejecucion actual, es decir, un objeto de rastreo (e.g., una funcion). 
    Un frame tiene los siguientes atributos:
    	* frame.f_lineno - la linea actual
    	* frame.f_locals - las variables actuales (es un dictionary)
    	* frame.f_code 	- el codigo actual (Code) que tiene el atributo frame.f_code.co_name (el nombre del la funcion actual)

    """
    def traceit(self, frame, event, arg):
        if self.our_frame(frame) or self.problematic_frame(frame):
            # No rastrearemos nuestros propios metodos
            pass
        else:
            self.log(event, frame.f_lineno, frame.f_code.co_name, frame.f_locals)
        return self.traceit


    # Es como un print(), pero siempre lo manda a archivo dado en la inicializacion (self.file), que por defecto es la consola.
    def log(self, *objects, sep: str = ' ', end: str = '\n', flush = True):
        print(*objects, sep = sep, end = end, file = self.file, flush = flush)



def remove_html_tags(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out



with Tracer():
    remove_html_tags("<b>abc</b>")