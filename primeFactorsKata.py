def primeFactors(number):
    numerosr = int(number)
    factors = []
    while numerosr != 1:
        for n in range (2, numerosr + 1):
            while numerosr % n == 0:
                numerosr /= n
                factors.append(n)
            if numerosr == 1:
                return factors
    return factors
