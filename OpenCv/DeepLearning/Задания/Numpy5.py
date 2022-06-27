"""
Задан двумерный массив X. Для каждой строчки массива X необходимо сделать следующее преобразование.

Пусть дана строчка x. Необходимо построить новый массив, где все элементы с нечетными индексами требуется заменить на число aa (значение по умолчанию a = 1a=1). Все элементы с четными индексами нужно возвести в куб. Затем записать элементы в обратном порядке относительно их позиций. В конце требуется слить массив xx с преобразованным xx и вернуть на выход функции (естественно, выход должен быть numpy-массивом).

Напишите функцию, которая выполняет данное преобразование для каждой строчки двумерного массива X. Массив X при этом должен остаться без изменений.

Используйте библиотеку numpy.
"""

import numpy as np
import copy

def transform(X, a=1):
    """
    param X: np.array
    """
    result = []
    
    if len(X.shape) == 1:
        X = np.expand_dims(X, axis=0)
    
    for idx, arr in enumerate(X):
        Y = copy.deepcopy(arr)
        Y[1::2] = a
        Y[::2] = arr[::2]**3
        Y = Y[::-1]
        result.append(np.hstack((arr,Y)))
    
    return result
