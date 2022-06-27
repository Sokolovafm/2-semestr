def almost_double_factorial(n):
    res = 1
    for i in range(1, n+1, 2):
        res *= i
    return res
