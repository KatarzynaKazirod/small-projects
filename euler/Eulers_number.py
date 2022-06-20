import math

def EulersNumber(precision):
    fsum = 1
    for i in range(1, precision + 1):
        factorials = 1/math.factorial(i)
        fsum = fsum + factorials
    return fsum

print(EulersNumber(100))