prix_u = int(input("Entrez le prix unitaire de votre achat :"))
q = int(input("Entrez la quantité de votre achat :"))
montant = prix_u*q


if montant < 10000 :
    remise = montant*0
else:
    if montant > 10000 and montant <= 50000:
        remise = montant * 0.05
    else:
        if montant > 50000:
            remise = montant * 0.1
montant_final = montant - remise
print (f"vous avez acheté un total de {montant} F CFA une remise de {remise} F CFA s'applique et cela vous fera donc : {montant_final} FCFA ") 
