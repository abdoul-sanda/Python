n = int(input("Entrez un entier naturel n  compris entre 1 et 10 : "))

while n < 1 or n > 10 :
    n= int(input("Veuillez saisir une valeur de n correcte:"))
for i in range (1,10) :
    print(f"{n}x{i}= {n*i}")