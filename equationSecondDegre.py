import math
from nosFonctions import *

#on utilise ici, notre fonction qui permet de recuperer un
#chiffre entier tape au clavier
a = tapezEntier()
b = tapezEntier()
c = tapezEntier()

#on sait que pour resoudre l'equation, on doit trouver le delta (google)
delta = (b*b) - 4*a*c #ici, la formule trouve sur google
print("le delta = ", delta)

if delta > 0 :
    print ("2 valeurs possible.")
    #si delta est plus grand que 0, on sait qu'on a 2 reponses
    # et qu'il faut utilise les formules suivantes (google)
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    print("x1 = ",x1," x2= ",x2)

elif delta == 0 :
    print ("1 valeur possible")
    #si delta est egale a 0, on sait qu'on a 1 reponse
    # et qu'il faut utilise la formule suivante (google)
    x1 = -b  / (2*a)

    print("x = ",x1)

else:
    print("pas de réponse.")
    