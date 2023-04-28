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


    ### MUTA TESTS

    def test8(self):
        clock = ClockDisplay([24, 60, 60])
        clock.increment()
        assert clock.str() == "00:00:01"

    def test9(self):    # testea línea 12 en clockdisplay mutacion and -> or
        clock = ClockDisplay([24, 60])
        clock.numbers = []
        clock.increment()
        assert clock.str() == ""

    def test11(self):
        clock = ClockDisplay([24, 60])
        clock.numbers[1].increase()
        assert clock.numbers[1].str() == "01"

    def test12(self):
        clock = ClockDisplay([24, 60])
        clock.numbers[1].value = 100
        assert clock.numbers[1].str() == "100"

    def test13(self):   # display_number 21: mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
        clock = ClockDisplay([24, 60])
        clock.numbers[1].value = 60
        clock.numbers[1].limit = 60
        assert clock.numbers[1].invariant() is False

    def test14(self):    # display_number 21: mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
        clock = ClockDisplay([24, 60])
        clock.numbers[1].value = 61
        clock.numbers[1].limit = 60
        assert clock.numbers[1].invariant() is False

    def test15(self):   # display_number 9: mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
        clock = ClockDisplay([24, 60])
        clock.numbers[1].value = -1
        assert clock.numbers[1].increase() is True

    def test16(self):   # display_number 9: mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
        clock = ClockDisplay([24, 60])
        clock.numbers[1].limit = -60
        assert clock.numbers[1].increase() is False

    def test17(self):   # display_number 16: mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
        clock = ClockDisplay([24, 60])
        clock.numbers[1].value = 10
        assert clock.numbers[1].str() == "10"

    def test18(self):
        # display_number 8: mutation from <class 'ast.Add'> to <class 'ast.Mod'
        # display_number 8: mutation from <class 'ast.Add'> to <class 'ast.Sub'>
        # Se supone que no hay valores x e y que cumplan
        # (x + y + 1) % y != (x % y + 1) % y
        # (x + y + 1) % y != (x - y + 1) % y
        number = NumberDisplay(3, 5)
        assert number.increase() is False
        assert number.value == 4

    def test19(self):   # clock_display 12: currentDisplay >= 0 mutation >= a >
        clock = ClockDisplay([24, 60])
        clock.numbers = []
        number = NumberDisplay(3, 5)
        clock.numbers.append(number)
        clock.increment()
        assert clock.str() == "04"


if __name__ == '__main__':
    unittest.main()
