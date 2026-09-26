### Aires d'un carré et d'un rectangle

liste= ['rectangle', "carré"]

choix = input ("Choiissez l'une des figures suivantes:")



def rect(l, L):
    return(l+L)*2

def square(c):
    return c**4



if choix = liste[0]:
    l = int(input("La largeur du triangle:"))
    L = int(input("La longueur du triangle:"))
    print(rect(l, L))


if choix = liste[2]:
    c = int(input("Le côté du carré:"))
    square(c)
    

print(f"L'aire du {choix} est : {square(c)}")


















l = int(input("Entrez la longueur du côté du carré:"))
print("L'aire du carré est:", square(l))  
