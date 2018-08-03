#on cree un variable qui est egal a 5
boite = 5

#si la variable boite est plus grande que 10
if boite > 10 :
    #on affiche plus grand
    print("plus grand")
# sinon, si la variable boite est plus petit que 10
elif boite < 10 :
    print("plus petit")
# sinon, en definitif, c'est que la variable est egale
else:
    print("egal")


#------------------
#exemple 2

#on garde le reste de la division de 52 par 2 (le modulo)
#et on stoque le resultat dans la variable boite
boite = 52 % 2

#si le contenu de la variable boite est egale a 0
#ATTENTION, double = quand on compare 2 elements
if boite == 0 :
    print("52 est un chiffre pair")