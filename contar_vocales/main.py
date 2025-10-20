vocales = "aeiou"
def contar_vocales(s):
    cantidad_vocales = 0

    for i in range(len(s)):
        if(s[i] in vocales):
            cantidad_vocales += 1

    return cantidad_vocales
