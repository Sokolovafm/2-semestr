"""
Фейсконтроль
На вход программе подается слово, необходимо проверить, начинается ли оно с большой буквы, если да - вывести на первой строке вердикт yes, а на следующей - слово без изменений. Если же слово начинается с маленькой буквы, на первой строке нужно вывести вердикт no, а на следующей строке - слово, первая буква которого переведена в верхний регистр.
"""

w = input()
if (w[0].isupper()):
    print("yes" + "\n" + w)
else:
    print("no" + "\n" + w.capitalize())