import sys
import ast
import traceback
from stackInspector import StackInspector

""" Clase para rastrear funciones que fueron ejecutadas. Para su uso, considere:
with CoverageTracer() as coverage:
    function_to_be_traced()

coverage.report_executed_lines()
"""

class CoverageTracer(StackInspector):

    def __init__(self):
        super().__init__(None, self.traceit)
        self.executed_lines = []

    # función que rastrea línea de código ejecutadas
    def traceit(self, frame, event: str, arg):
        if event == "line":
            function_name = frame.f_code.co_name
            n_line = frame.f_lineno 

            # No debemos rastrearnos a nosotros
            if not self.our_frame(frame) and not self.problematic_frame(frame):
                self.executed_lines.append((function_name, n_line))

        return self.traceit     


    def report_executed_lines(self): # Funciona bien
        result = set(self.executed_lines)
        return sorted(result, key=lambda a: a[1])


    def report_execution_count(self):
        result = self.executed_lines
        aux_list = []
        result2 = []

        for i in range(len(result)):
            # si es nuevo:
            if result[i] not in aux_list:
                aux_list.append(result[i])
                result2.append((result[i][0], result[i][1], 1))
            else:
                for j in range(len(result2)):
                    if (result[i][0] == result2[j][0] and result[i][1] == result2[j][1]):
                        # tuplas son inmutables, así que tenemos que
                        # crear nueva tupla con contador actualizado 
                        result2[j] = (result[i][0], result[i][1], result2[j][2]+1)
        

        return sorted(result2, key=lambda a: a[1])



