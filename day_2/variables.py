# Niveau 1 
#Jour 2 : 30 jours de programmation Python 
prénom = "Ndeya"
nom = "Ndiaye"
nom_complet = "Mbasse" 
pays = "Sénégal" 
ville = "Dakar"
age = 21 
<< année >> = 2026
`is_married` = " je le suis "
 `is_true` = 2
`is_light_on` = "allumer"
prenom , nom , date , numero = "cheikh" , "diaw" , 02/12 , 0744738538
# 1 Vérifiez le type de données de toutes vos variables à l'aide de la fonction intégrée type().
type("prénom")
type("nom")
type("nom_complet")
type("pays")
type("ville")
type("age")
type("<< annee >>")
type("`is_married`")
type(" `is_true`")
type("`is_light_on`")
# 2 Utilisez la fonction intégrée len() pour trouver la longueur de votre prénom.
longueur_prenom = len(prenom)
# 3 Comparez la longueur de votre prénom et de votre nom de famille
prenom = "Ndeya"
nom = "Ndiaye"

# On calcule les longueurs avec len()
longueur_prenom = len(prenom)
longueur_nom = len(nom)

# On compare les deux longueurs
if longueur_prenom > longueur_nom:
    print("Le prénom  est plus long que le nom.")
elif longueur_prenom < longueur_nom:
    print("Le nom  est plus long que le prénom.")
else:
    print("Le prénom et le nom ont la même longueur.")
 # 4 Déclarez 5 comme num_one et 4 comme num_two
num_one = 5
num_two = 4
# 5 Additionnez num_one et num_two et assignez le résultat à la variable total.
total = num_one + num_two
print("variable_total :", total)
# 6 Soustrayez num_two de num_one et assignez la valeur à la variable diff.
soustraction = num_one - num_two 
print("variable_diff :", soustraction)
# 7 Multipliez num_two et num_one et affectez la valeur à une variable produit
produit = num_one * num_two
print("variable_produit :" , produit)
# 8 Divisez num_one par num_two et assignez la valeur à une variable division.
division = num_one / num_two
print("variable_division :" , division)
# 9 Utilisez la division modulo pour calculer num_two divisé par num_one et assignez le résultat à la variable remainder.
division_modulo = num_two % num_one
print("variable_remainder :" , division_modulo)
# 10 Calculez num_one à la puissance num_two et assignez la valeur à une variable exp.
exp = num_one ** num_two
print("exp :", exp)


