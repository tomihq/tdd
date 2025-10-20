def factorial(n):
    if(n<0):
        return "number must be positive"
    elif(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)
