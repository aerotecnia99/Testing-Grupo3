import unittest
#importar módulos a testear.
from src.clock_factory import *
from src.display_number import *

''' Tests que buscan 100% coverage.
'''

class TestSrc(unittest.TestCase):

    ## TEST UNITARIOS: INSTANCIAS TODAS LAS CLASES DEL PROYECTO

    ## TESTS NUMBER DISPLAY
    def test1(self):
        display = NumberDisplay(10, 20)
        display.increase() ## value = 11 -> False
        result = display.str()
        self.assertEqual(result, "11")

    def test2(self):
        display = NumberDisplay(10, 20)
        display.reset() ## 00
        result = display.str() ## explora todos los casos del str()
        self.assertEqual(result, "00")

    def test3(self):
        display = NumberDisplay(9, 20)
        result = display.invariant()
        self.assertEqual(result, True)

    def test4(self):
        # que clone correctamente
        display = NumberDisplay(10, 20)
        display_clonado = display.clone()
        result = display_clonado.str()
        self.assertEqual(result, "10")

        
    # ## TESTS CLOCK DISPLAY

    def test5(self):
        # que incremente corectamente cuando se alcanza limite
        # del secundero.

        ## entregamos iterable con límite valor de cada rango
        ## hh:mm:ss:mmmm
        ## hh:mm:ss
        ## hh:mm

        clock_display = ClockDisplay([24,60,60])
        clock_display.numbers = [NumberDisplay(0,24), 
                                NumberDisplay(0,60),
                                NumberDisplay(59,60)]
        clock_display.increment()
        result = clock_display.str()
        self.assertEqual(result, "00:01:00")
        

    def test6(self):
        clock_display = ClockDisplay([24,60,60])
        clock_clonado = clock_display.clone()
        result = clock_clonado.str()
        self.assertEqual(result, "00:00:00")

    def test7(self):
        clock_display = ClockDisplay([24,60,60])
        clock_display.numbers = [NumberDisplay(23,24), 
                                NumberDisplay(59,60),
                                NumberDisplay(59,60)]
        result = clock_display.invariant()
        self.assertEqual(result, True)


    ##obs: list(map(fx, iterable))
        ## fx se aplica sobre cada elemento del iterable  (map)
        ## y se retorna una lista

    ## all(iterable) -> retorna True solo si todos los elementos del
    #  iterable tienen un valor booleano de True o el iterable 
    #  está vacío, en los demás casos retornara False

    ## %: operación resto
