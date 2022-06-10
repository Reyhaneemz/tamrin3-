import random

araye = []

n = int(input("tole list: ")) 

for i in range(n):
    a = random.randint(1 , 10000)
    if a not in araye:
         araye.append(a)

print(araye)

