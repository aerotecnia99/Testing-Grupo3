import unittest
#importar módulos a testear.
from src.clock_factory import *
from src.display_number import *

''' Tests que buscan 100% coverage.
'''

class TestSrc(unittest.TestCase):

    def test1(self):
        clock = ClockDisplay([23,60])
        for i in range(20):
            clock.increment()
            print(clock.str())

    def test2(self):
        clock = ClockDisplay([23,60])
        for i in range(20):
            clock.increment()
        clock.clone()
        print(clock.str())
    
    def test3(self):
        clock = ClockDisplay([23,60])
        for i in range(50):
            clock.increment()
        clock.invariant()
        print(clock.str())

    def test4(self): #testea linea 13 clockdisplay
        clock = ClockDisplay([23,60])
        for i in range(250):
            clock.increment()

    def test5(self):
        clock = ClockDisplay([23,60])
        clock.increment()
        # resetear clock:
        clock_reseteado = list(map(lambda n: n.reset(), clock.numbers))
        


if __name__ == '__main__':
    unittest.main()