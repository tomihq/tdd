def factores_primos(n):
    if(n == 0 or n == 1):
        return []
    elif(n == 2 or n == 3):
        return [n]
    
    factores_primos_n = []
    contador = 0
    while(contador < n):
        if(n % 2 == 0):
            factores_primos_n.append(2)
            n = n/2
        contador+=1
    return factores_primos_n
