### L'utilisateur entre 3 entiers et le programme en sort le maximum et le minimum 


x = int (input("Entrez un entier x :"))
y = int (input ("Entrez un second entier y:"))
z = int (input ("Entrez un troisième entier z :"))
moy = 0 

if x > y:
    max = x 
    min = y
else :
    max = y 
    min = x
if z > max : 
    moy = max 
    max = z 
else :
    if z > min :
        moy = z 
    else:
        if min > z :
            moy = min 
            min = z
    
print(f"{max} est le plus grand {moy} le moyen et le plus petit est {min}")
      
