"""
Нас интересуют только Аристотели
Вам необходимо написать программу, которая получает на вход два значения - имя человека (строка) и его возраст (число), каждое с новой строки. Если человека зовут Аристотель - необходимо вывести его возраст, в остальных случаях не нужно ничего выводить.
"""

name = input()
age = int(input())
if name == "Аристотель":
    print(age)
