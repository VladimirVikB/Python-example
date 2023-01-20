import random
from string import ascii_lowercase, ascii_uppercase

#Вводится натуральное число N. Используя строки из латинских букв
# ascii_lowercase и ascii_uppercase:
#задайте функцию-генератор, которая бы возвращала случайно сформированные
# email-адреса с доменом mail.ru и длиной в N символов. Например, при N=6,
# получим адрес: SCrUZo@mail.ru
#Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
#Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать
# постоянно. Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
random.seed(1)
n = int(input())


def get_mail(n):
    while True:
        mail = ""
        for i in range(n):
            indx = random.randint(0, len(chars) - 1)
            mail += chars[indx]
        yield mail + "@mail.ru"


gen = get_mail(n)
for i in range(5):
    print(next(gen))