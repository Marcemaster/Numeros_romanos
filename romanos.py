
simbolos = {
    'unidades': ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', ],
    'decenas': ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ],
    'centenas': ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ],
    'millares': ['', 'M', 'MM', 'MMM'],
}

romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def validar_n(n):
    if not isinstance(n, int):
        raise ValueError("{} debe ser un entero".format(n))

    if n < 0 or n > 3999:
        raise ValueError("{} debe estar entre 0 y 3999".format(n))


def a_romano(n):
    validar_n(n)
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


def a_numero(n):
    acumulador = 0
    valorAnt = 0
    cuenta_repeticiones = 0
    resta = 0
    for caracter in n:
        valor = romanos[caracter]

        if valorAnt and valor > valorAnt:
            if cuenta_repeticiones > 0:
                raise ValueError(
                    "No se pueden hacer restas dentro de repeticiones")
            if valorAnt in (5, 50, 500):
                raise ValueError("No se pueden restar V, L, D")
            if valor > 10*valorAnt:
                raise ValueError(
                    "No se pueden restar entre dígitos 10 veces mayores.")
            if resta > 0:
                raise ValueError("No se pueden restar dos numeros seguidos")

            else:
                acumulador += (valor - valorAnt*2)
                resta += 1
        else:
            acumulador += valor
            resta = 0

        if valor == valorAnt:
            if valor in (5, 50, 500):
                raise ValueError("No se puede repetir V, L ó D")
            cuenta_repeticiones += 1
            if cuenta_repeticiones == 3:
                raise ValueError(
                    "Demasiadas repeticiones de {}".format(caracter))
        else:
            cuenta_repeticiones = 0

        valorAnt = valor

    return acumulador
