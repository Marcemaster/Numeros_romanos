import unittest
from romanos import a_numero


class RomanosTest(unittest.TestCase):
    def test_romanos(self):
        self.assertEqual(a_numero('I'), 1)
        self.assertEqual(a_numero('V'), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero('XXV'), 25)
        self.assertEqual(a_numero('XXIV'), 24)

    def test_no_se_restan_VLD(self):
        with self.assertRaises(ValueError):
            a_numero('VC')

    def test_no_se_resta_mas_de_un_orden(self):
        self.assertEqual(a_numero('IV'), 4)
        self.assertEqual(a_numero('IX'), 9)
        self.assertEqual(a_numero('XL'), 40)
        self.assertEqual(a_numero('XC'), 90)
        self.assertEqual(a_numero('CD'), 400)
        self.assertEqual(a_numero('CM'),900)
        with self.assertRaises(ValueError):
            a_numero('IL')
            a_numero('IC')
            a_numero('IM')
            a_numero('XM')
            a_numero('XD')
        
