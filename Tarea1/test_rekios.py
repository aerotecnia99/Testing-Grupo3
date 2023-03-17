import unittest
from model import *
from myparser import *
from metrics import *


class TestParser(unittest.TestCase):
    ### OJITOOO
    ## En operación modular "a mod b", b>0 !!\
    ## Resto también debe ser positivo.
    
    # Test Mix Operaciones Unarias y Binarias
    def test_mix_bin_una(self):
        ast = parser("(+ (++ 7) (% (-- 42) (- (++ 12) 3)))")
        result = ast.eval()
        self.assertEqual(result, 9)

    def test_mix_bin_una2(self):
        ast = parser("(+ (++ 7) (% (- 1 22) (- (++ 53) 50)))")
        result = ast.eval()
        self.assertEqual(result, 11)

    def test_mix_una_bin(self):
        ast = parser("(++ (+ (% (- (-- 9) 2) 5) 21))")
        result = ast.eval()
        self.assertEqual(result, 23)

    # Test PP, Resta -> Parser
    def test_pp_resta(self):
        ast1 = SubtractionNode(PlusPlusNode(NumberNode(10)), NumberNode(10))
        ast2 = parser("(- (++ 10) 10)")
        self.assertEqual(ast1, ast2)

    # Test PP, Resta -> Result
    def test_pp_resta2(self):
        ast = parser("(- (++ 10) 10)")
        result = ast.eval()
        self.assertEqual(result, 1)

    
    


if __name__ == '__main__':
    unittest.main()