"""
Гастрономические предпочтения снежного человека
У снежного человека есть два любимых блюда - вафли и шпинат, которые он признает именно в этой последовательности потребления, а людей с полностью совпадающими гастрономическими вкусами называет красавчиками. Вам необходимо написать программу, которая будет получать на вход два значения - названия любимых блюд пользователя и проверять, совпадают ли они с любимыми блюдами снежного человека, в случае полного совпадения нужно сообщить пользователю, что он красавчик.
"""

a = input()
b = input()

if (a == "вафли" and b == "шпинат"):
    print("красавчик")