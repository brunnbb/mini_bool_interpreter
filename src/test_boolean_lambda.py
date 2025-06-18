import unittest
from boolean_lambda import TRUE, FALSE, NOT, AND, OR, NAND, NOR, XOR, IF, resultado

class TestBooleanOperators(unittest.TestCase):

    def test_true(self):
        self.assertEqual(resultado(TRUE(1)(0)), 1)

    def test_false(self):
        self.assertEqual(resultado(FALSE(1)(0)), 0)

    def test_not(self):
        self.assertEqual(resultado(NOT(FALSE)), 'TRUE')
        self.assertEqual(resultado(NOT(TRUE)), 'FALSE')

    def test_and(self):
        self.assertEqual(resultado(AND(TRUE)(TRUE)), 'TRUE')
        self.assertEqual(resultado(AND(TRUE)(FALSE)), 'FALSE')
        self.assertEqual(resultado(AND(FALSE)(TRUE)), 'FALSE')
        self.assertEqual(resultado(AND(FALSE)(FALSE)), 'FALSE')

    def test_or(self):
        self.assertEqual(resultado(OR(TRUE)(TRUE)), 'TRUE')
        self.assertEqual(resultado(OR(TRUE)(FALSE)), 'TRUE')
        self.assertEqual(resultado(OR(FALSE)(TRUE)), 'TRUE')
        self.assertEqual(resultado(OR(FALSE)(FALSE)), 'FALSE')

    def test_nand(self):
        self.assertEqual(resultado(NAND(TRUE)(TRUE)), 'FALSE')
        self.assertEqual(resultado(NAND(TRUE)(FALSE)), 'TRUE')
        self.assertEqual(resultado(NAND(FALSE)(TRUE)), 'TRUE')
        self.assertEqual(resultado(NAND(FALSE)(FALSE)), 'TRUE')

    def test_nor(self):
        self.assertEqual(resultado(NOR(TRUE)(TRUE)), 'FALSE')
        self.assertEqual(resultado(NOR(TRUE)(FALSE)), 'FALSE')
        self.assertEqual(resultado(NOR(FALSE)(TRUE)), 'FALSE')
        self.assertEqual(resultado(NOR(FALSE)(FALSE)), 'TRUE')

    def test_xor(self):
        self.assertEqual(resultado(XOR(TRUE)(TRUE)), 'FALSE')
        self.assertEqual(resultado(XOR(TRUE)(FALSE)), 'TRUE')
        self.assertEqual(resultado(XOR(FALSE)(TRUE)), 'TRUE')
        self.assertEqual(resultado(XOR(FALSE)(FALSE)), 'FALSE')

    def test_if(self):
        self.assertEqual(resultado(IF(TRUE)(1)(2)), 1)
        self.assertEqual(resultado(IF(FALSE)(1)(2)), 2)

if __name__ == '__main__':
    unittest.main()