"""
Опять здороваемся 
На вход программе подается имя пользователя в произвольном регистре. Необходимо поприветствовать пользователя следующим образом, при этом упомянув в стандартном формате - первая буквы заглавная, остальные - строчные:

Привет, *введенное имя*!
"""

a = input()
print("Привет, " + a.capitalize() + "!")