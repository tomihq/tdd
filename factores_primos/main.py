def factores_primos(n):
    if(n == 0 or n == 1):
        return []
    
    factores_primos_n = []
    contador = 2
    while(contador <= n):
        if(n % contador == 0):
            factores_primos_n.append(contador)
            n = n/contador
        else:
            contador+=1
    return factores_primos_n
