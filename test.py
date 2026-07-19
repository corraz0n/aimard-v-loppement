import random

nombre_secret = random.randint(1, 10)

print("Devine le nombre entre 1 et 10")

while True:
    choix = int(input("Ton nombre : "))

    if choix == nombre_secret:
        print("Bravo tu as gagné !")
        break
    elif choix < nombre_secret:
        print("C'est plus grand")
    else:
        print("C'est plus petit")
