
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


def caracteres_correctos(n):
    for c in romanos.keys():
        c = c*4
        if c in n:
            return False
    return True


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
    caracterAnt = ""
    if caracteres_correctos(n):
        for caracter in n:
            valor = romanos[caracter]
            if valor > valorAnt:
                if valorAnt > 0 and n[n.index(caracterAnt)+1] == caracterAnt:
                    raise ValueError(
                        "No se puede restar dos veces al mismo número.")
                if valorAnt in (5, 50, 500):
                    raise ValueError("No se pueden restar V, L, D")
                if valorAnt > 0 and valor > 10*valorAnt:
                    raise ValueError(
                        "No se pueden restar entre dígitos 10 veces mayores.")

                else:
                    acumulador += (valor - valorAnt*2)

            else:
                acumulador += valor

            valorAnt = valor
            caracterAnt = caracter
        return acumulador
    else:
        raise ValueError(
            "Error, no se puede poner más de 3 veces el mismo caracter")
