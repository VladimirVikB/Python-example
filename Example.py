import random
from string import ascii_lowercase, ascii_uppercase

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