
x= int(input("Entrez un entier svp:"))

a=['+', '-', 'x', 'mod', '/']


y = int(input("Entrez un autre :"))

choix=input(f"laquelle de ces opérations {a} voulez vous faire ?")

if choix == a[0]:
    print(f"{x}+{y}={x+y}")
    
if choix == a[1]:
    print(f"{x}-{y}={x-y}")

if choix == a[2]:
    print(f"{x}x{y}={x*y}")
    
if choix == a[3]:
    print(f"{x} mod {y}={x%y}")
    
if choix == a[4]:
    if y == 0:
        print(f"Calcul impossible") 
    else:
        print(f"{x}+{y}={x-y}")
