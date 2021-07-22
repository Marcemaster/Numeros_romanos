import unittest
from romanos import RomanNumber

class RomanNumberClassTest(unittest.TestCase):
    def test_crear_Numero_romano(self):
        uno = RomanNumber(1)
        dos = RomanNumber('II')

        self.assertEqual(uno, 'I')
        self.assertEqual(dos, 'II')

        self.assertEqual(uno.valor, 1)