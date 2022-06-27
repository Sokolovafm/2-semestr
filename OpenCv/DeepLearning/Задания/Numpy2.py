"""
Вам подаются на вход два вектора a и b в трехмерном пространстве. Реализуйте их скалярное произведение с помощью numpy и без. 
"""

import numpy as np

def no_numpy_scalar(a, b):
    s = 0
    for x, y in zip(a, b):
        s += x * y
    return s

def numpy_scalar (a, b):
    a = np.array(a)
    b = np.array(b)
    return a.dot(b)
