import traceback
import sys
"""Clase que brinda funciones para facilitar la inspeccion de la pila"""
class StackInspector:

    def __init__(self, original, trace):
        self.original_trace_function = original
        self.trace_function = trace

    # Retorna verdad si el frame esta in la clase actual de inspeccion
    def our_frame(self, frame):
        return isinstance(frame.f_locals.get('self'), self.__class__)

    # Retorna verdad si el frame esta involucrado con un <module>
    def problematic_frame(self, frame):
        return frame.f_code.co_name == "<module>"

    # Retorna verdad si alguna excepcion fue generada por el StackInspector o alguna de sus subclases
    def is_internal_error(self, exc_tp, exc_value, exc_traceback):
        if not exc_tp:
            return False

        for frame, lineno in traceback.walk_tb(exc_traceback):
            if self.our_frame(frame):
                return True

        return False

    def traceit(self, frame, event: str, arg):
        pass

    # Esta funcion se llama al comienzo de un bloque 'with' y comienza con el rastreo
    def __enter__(self):
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.trace_function)

        return self

    # Esta funcion se llama al final de un bloque 'with' y termina el rastreo.
    # Retorna 'None' si todo funciona bien y si retorna 'False' significa que hubo un error interno (por nuestra clase Tracer o subclases). 
    def __exit__(self, exc_tp, exc_value, exc_traceback):
        sys.settrace(self.original_trace_function)

        # Note que debemos retornar un valor 'False' para indicar que hubo un error interno y levantar las excepciones correspondientes.
        if self.is_internal_error(exc_tp, exc_value, exc_traceback):
            return False
        else:
            # Significa que todo funciona bien
            return None

