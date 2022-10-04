import random
#input
X=int(input("intenta adivinar mi numero: "))
#processing
A=random.randint(1,100)
i=0
while  A!=X:
    i=i+1
    X=int(input("intenta adivinar mi numero: "))
    if X<A:
        print(" El numero a adivinar  es mas grande")
    elif X>A:
        print("El numero a adivinar es mas pequeño")
    elif X==A:
        print("Felicitaciones has adivinado el numero el numero era " , A,"en" ,i,"intentos")