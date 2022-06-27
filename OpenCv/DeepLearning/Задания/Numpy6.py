"""
С помощью numpy написать функцию для кодирования массива (Run-length encoding). Все подряд повторения элементов функция сжимает в один элемент и считает количество повторений. Функция возвращает кортеж из двух numpy-векторов одинаковой длины. Первый содержит элементы, а второй — сколько раз их нужно повторить.
"""

import numpy as np
def encode(a):
    ia = np.asarray(a)
    n = len(ia)
    if n == 0: 
        return (None, None)
    else:
        y = np.array(ia[1:] != ia[:-1])
        i = np.append(np.where(y), n - 1)
        z = np.diff(np.append(-1, i))
        return(ia[i], z)
