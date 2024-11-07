"""
Ce module contient des fonctions pour vérifier si un nombre est premier
"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Retourne un booléen exprimant la vérité de « p est un nombre premier ».

    Args:
        p: valeur entière positif

    Returns: 
        le booléan premier.

    >>> isprime(-1)
    'p must be strictly positive'
    >>> isprime(1)
    False
    >>> isprime(15)
    False
    """
    # votre code ici
    premier = True
    if p in (0,1):
        premier = False
        return premier
    if p < 0:
        return 'p must be strictly positive'
    # parcourt les diviseurs de p pour vérifier si p est premier
    for i in range(2,int(sqrt(p)+1)):
        if p % i == 0:
            return False
    return premier


#### Fonction principale


def main():
    """
    Fonction principale pour tester les fonctions secondaires 
    dont isprime
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
    nombre_test = int(input("Entrez le nombre à tester: " ))
    if isprime(nombre_test):
        print("True")
    else:
        print("False")
    print()


if __name__ == "__main__":
    main()
