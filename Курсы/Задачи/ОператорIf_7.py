"""
Последнее на кошачьем
Ну и последняя группа чисел, попадающих под Славины критерии красоты, должна делиться на 7, не делиться на 2 и не равняться 21-му, если число удовлетворяет этим условиям, нужно вывести "красивое".
"""

a = int(input())
if (a % 7 == 0 and a % 2 != 0 and a != 21):
    print("красивое")