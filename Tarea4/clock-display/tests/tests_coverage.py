# import unittest
# #importar módulos a testear.
# from src.clock_factory import *
# from src.display_number import *

# ''' Tests que buscan 100% coverage.
# '''

# class TestSrc(unittest.TestCase):

#     def test1(self):
#         clock = ClockDisplay([23,60])
#         for i in range(20):
#             clock.increment()
#             # print(clock.str())

#     def test2(self):
#         clock = ClockDisplay([23,60])
#         for i in range(20):
#             clock.increment()
#         clock.clone()
#         # print(clock.str())
    
#     def test3(self):
#         clock = ClockDisplay([23, 60])
#         for i in range(50):
#             clock.increment()
#         clock.invariant()
#         # print(clock.str())

#     def test4(self):    # testea linea 13 clockdisplay
#         clock = ClockDisplay([23, 60])
#         for i in range(250):
#             clock.increment()

#     def test5(self):
#         clock = ClockDisplay([23, 60])
#         clock.increment()
#         # resetear clock:
#         clock_reseteado = list(map(lambda n: n.reset(), clock.numbers))

#     def test6(self):    # testea línea 12 en clockdisplay
#         clock = ClockDisplay([24,60])
#         clock.numbers = []
#         clock.increment()

#     def test7(self):
#         clock = ClockDisplay([24, 60, 60])
#         for i in range(4):
#             clock.increment()
#         assert clock.str() == "00:00:04"

#     def test8(self): # NO FUNCIONANDO
#         print("TEST 8")
#         clock = ClockDisplay([24, 60])
#         print(clock.str())
#         print(clock.numbers[0].str())
#         print(clock.numbers[1].str())
#         clock.numbers.pop()
#         print(clock.str())
#         print("largo", len(clock.numbers) - 1)
#         clock.increment()

#     def test9(self):
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].increase()
#         assert clock.numbers[1].str() == "01"

#     def test10(self):
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].value = 100
#         assert clock.numbers[1].str() == "100"

#     def test11(self):   # display_number 21: mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].value = 60
#         clock.numbers[1].limit = 60
#         assert clock.numbers[1].invariant() is False

#     def test12(self):    # display_number 21: mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].value = 61
#         clock.numbers[1].limit = 60
#         assert clock.numbers[1].invariant() is False

#     def test13(self):   # display_number 9: mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].value = -1
#         assert clock.numbers[1].increase() is True

#     def test14(self):   # display_number 9: mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].limit = -60
#         assert clock.numbers[1].increase() is False

#     def test15(self):   # display_number 16: mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
#         clock = ClockDisplay([24, 60])
#         clock.numbers[1].value = 10
#         assert clock.numbers[1].str() == "10"

#     def test16(self):   # display_number 8: mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
#         # display_number 8: mutation from <class 'ast.Add'> to <class 'ast.Mod'
#         # display_number 8: mutation from <class 'ast.Add'> to <class 'ast.Sub'>
#         # Se supone que no hay valores x e y que cumplan
#         # (x + y + 1) % y != (x % y + 1) % y
#         # (x + y + 1) % y != (x - y + 1) % y
#         number = NumberDisplay(3, 5)
#         assert number.increase() is False
#         assert number.value == 4


# if __name__ == '__main__':
#     unittest.main()