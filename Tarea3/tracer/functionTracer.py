import sys
import ast
import inspect
from types import *
import traceback
from stackInspector import StackInspector

""" Clase para rastrear funciones que fueron ejecutadas. Para su uso, considere:
with FunctionTracer() as funTracer:
    function_to_be_traced()

funTracer.report_executed_functions()
"""

class FunctionTracer(StackInspector):

    def __init__(self):
        super().__init__(None, self.traceit)
        self.executed_functions = []

    # Funcion que rastrea el codigo
    def traceit(self, frame, event: str, arg):
        if event == "call":
            function_name = frame.f_code.co_name
            line = frame.f_lineno

            # Evitamos rastrearnos a nosotros 
            if not self.our_frame(frame) and not self.problematic_frame(frame):
                self.executed_functions.append((function_name, line))

        return self.traceit

    def report_executed_functions(self):
        result = set(self.executed_functions)
        return sorted(result, key=lambda a: a[1])

