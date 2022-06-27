"""
Перемножение матриц
Напишите две функции, каждая из которых перемножает две квадратные матрицы: одна без использования встроенных функций numpy, а другая --- с помощью numpy. На вход первой задаче подаются списки размера size по size элементов в каждом. На вход второй задаче подаются объекты типа np.ndarray --- квадратные матрицы одинакового размера. 

Первая функция должна возвращать список списков, а вторая -- np.array.
"""

import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """
    rows_first = len(first)
    cols_first = len(first[0])
    rows_second = len(second)
    cols_second = len(second[0])
    
    if cols_first != rows_second:
        return []
    
    a = [[0 for row in range(cols_second)] for col in range(rows_first)]

    for i in range(rows_first):
        for j in range(cols_second):
            for k in range(cols_first):
                a[i][j] += first[i][k]*second[k][j]
    result = a 
    return result

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """
    result = np.dot(first, second)
    return result
