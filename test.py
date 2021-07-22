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
            a_numero('LD')
            a_numero('DM')

    def test_no_se_resta_mas_de_un_orden(self):
        self.assertEqual(a_numero('IV'), 4)
        self.assertEqual(a_numero('IX'), 9)
        self.assertEqual(a_numero('XL'), 40)
        self.assertEqual(a_numero('XC'), 90)
        self.assertEqual(a_numero('CD'), 400)
        self.assertEqual(a_numero('CM'), 900)
        with self.assertRaises(ValueError):
            a_numero('IL')
        with self.assertRaises(ValueError):
            a_numero('IC')
        with self.assertRaises(ValueError):
            a_numero('IM')
        with self.assertRaises(ValueError):
            a_numero('XM')
        with self.assertRaises(ValueError):
            a_numero('XD')

    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(a_numero('III'), 3)
        with self.assertRaises(ValueError):
            a_numero('IIII')
        with self.assertRaises(ValueError):
            a_numero('VVVV')
        with self.assertRaises(ValueError):
            a_numero('XXXX')
        with self.assertRaises(ValueError):
            a_numero('CCCC')
        with self.assertRaises(ValueError):
            a_numero('DDDD')

    def test_no_resta_dos_iguales(self):
        with self.assertRaises(ValueError):
            a_numero('CCM')
        with self.assertRaises(ValueError):
            a_numero('XXL')
        with self.assertRaises(ValueError):
            a_numero('IIV')
        with self.assertRaises(ValueError):
            a_numero('IIX')
        with self.assertRaises(ValueError):
            a_numero('CCCD')


    def test_no_repeticiones_V(self):
        with self.assertRaises(ValueError):
            a_numero('VV')
        with self.assertRaises(ValueError):
            a_numero('MDVVV')
        with self.assertRaises(ValueError):
            a_numero('MMDDCC')

    def restar_dos_veces_seguidas(self):
        with self.assertRaises(ValueError):
            a_numero('IXC')
        with self.assertRaises(ValueError):
            a_numero('XCM')
        with self.assertRaises(ValueError):
            a_numero('MIXC')