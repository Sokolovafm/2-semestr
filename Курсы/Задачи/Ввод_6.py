"""
Ценная пыль
Бяки решили коллекционировать пылинки, но поскольку они очень дружны между собой, да еще и щепетильны до жути по сути своей, все собранные пылинки они решили делить поровну до мини-микро-нано частиц каждой пылинки. На вход программе подается два числа - количество пылинок, которое удалось найти Бякам и количество самих Бяк-коллекционеров. Необходимо вывести число - сколько пылинок достанется каждой Бяке в следующем формате:

Вот по столечко *кол-во пылинок* пылинок достанется каждой Бяке
"""

a = int(input())
b = int(input())
print("Вот по столечко " + str(a / b) + " пылинок достанется каждой Бяке")