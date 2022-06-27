"""
Дан список текстов, слова в которых разделены пробелами (можно считать, что знаков препинания нет). Часть слов является "мусорными": в них присутствуют цифры и спецсимволы. Отфильтруйте такие слова из каждого текста.

Используйте функции str.split, str.isalpha, str.join, а также list comprehensions.

Пример ввода:

['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']

Пример вывода: 

['thousand devils', 'My name is', 'Room costs', '']

В этом задании функция print вам не понадобится. Результаты выполнения функций нужно возвращать, а не печатать!

Если в тексте все слова являются мусорными, текст должен преобразоваться в пустую строку.
"""

def process(sentences):
    #YOUR CODE

    result = list(map(lambda n : ' '.join(filter(lambda n: n.isalpha(),n.split())),sentences))
    return result
