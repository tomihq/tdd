def fizzbuzz(n):
    if(n%3 == 0 and n%5 == 0):
        return "fizzbuzz"
    elif(n%3 == 0):
        return "fizz"
    elif(n%5 == 0):
        return "buzz"
    return str(n)
