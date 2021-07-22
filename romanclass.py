
class RomanNumber():
    def __init__(self):

        if isinstance(valor, int):
            self.valor = valor
            self.cadena = self.a_romano(valor)


def validar_n(self, n):
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n < 0 or n > 3999:
        raise ValueError("{} debe estar entre 0 y 3999".format(n))



    def a_romano(self):
        self.validar_n(self.valor)
        c = str(n)
        c = c[::-1]

        unidades = 0
        decenas = 0
        centenas = 0
        millares = 0

        if len(c) >= 1:
            unidades = int(c[0])
        if len(c) >= 2:
            decenas = int(c[1])
        if len(c) >= 3:
            centenas = int(c[2])
        if len(c) == 4:
            millares = int(c[3])

        componentes = (millares, centenas, decenas, unidades)

        return simbolos['millares'][millares] + simbolos['centenas'][centenas] + simbolos['decenas'][decenas] + simbolos['unidades'][unidades]

    

    