import streamlit as st


st.set_page_config(
    page_icon=":snake:",
)
st.markdown("<h1 style='text-align: center; color: black;'>Les variables</h1>", unsafe_allow_html=True)



st.image("https://geekflare.com/wp-content/uploads/2021/11/system-environment-variables.png")
st.markdown("""

### Déclarer une variable

""")
code = """
formateur = "Charles"

nombre_apprenants = 12

# double déclaration
apprenant = eleve = "Antoine"
print(eleve)
print(apprenant)
apprenant = "Patrick"
print(eleve)
print(apprenant)
"""
st.code(code, language="python")


st.markdown("""
### Afficher une variable
""")

code = """
# affichage d'une variable
print(formateur)

# affichage de plusieurs éléments 
print("nombre_apprenants:",  nombre_apprenants)

# commentaire avec l'attribut format
print( "{} a {} dans ma formation, dont:  {}".format(formateur,nombre_apprenants,apprenant))

# Ex : Emad
myList = ["Emad", "Mira", "Zainab"]
print( "{} a {} dans ma formation, dont:  {}".format(*myList))   # le "*" ici est pour dir quon a une list ici à imprimer

# commentaires avec les f-strings
print( f"{formateur} a {nombre_apprenants} dans ma formation, dont:  {apprenant}")

print (f"{formateur=}")   # Attention, il y a = à la fin

"""
st.code(code, language="python")

st.markdown("""
### Modifier une variable
""")

code = """
apprenant = eleve = "Antoine"
eleve = "Denis"
nombre_apprenants = nombre_apprenants + 2
nombre_apprenants += 2

print("nombre_apprenants: ", nombre_apprenants) #nombre_apprenants:  20
print("apprenant: ", apprenant)  #apprenant:  Antoine
print("eleve: ", eleve)  # eleve:  Denis

eleve = 7
print(eleve) # 7
"""
st.code(code, language='python')

st.markdown("""
### Supprimer une variable
""")

code = """
del apprenants
"""
st.code(code, language='python')

st.markdown("""
### Nommer une variable avec la Pep-8

- Mettez un espace avant et après le signe égal
   - apprenant = "Charles" et non apprenant="Charles"
- Utilisez des noms descriptifs dans votre code.
   - exemple: Au lieu de  quantite  (ou pire,qte), ajoutez des détails :quantite_en_stock,solde_actuel, etc.
- Utilisez des mots complets.
   - exemple,revenu_annuelest plus clair querev_annuel.
- Suivez une convention d’appellation commune.
   - le snake case : des noms composés de plusieurs mots séparés par des tirets bas(_)
      - exemple nombre_de_chats,  reponse_finale  ,  le_meilleur_developpeur_python_du_monde, etc.
   - commencez avec une lettre minuscule (surtout pas par un nombre)
   - Utilisez uniquement des caractères alphanumériques et des tirets bas... et donc pas d'accents !
- N’oubliez pas que les noms de variables sont sensibles à la casse.
   - age,  Age  et  AGE  sont trois variables différentes. 

### S'exercer à manipuler les variables
**`Exercice`**: créez l'état civil de votre voisin 
- déclarer les variables nom, prénom et deuxième prénom puis une variable nom complet à l'aide des trois précédentes en les concaténant à l'aide de l'opérateur + 
- déclarer les variables année actuelle et année de naissance puis créer la variable âge à l'aide des deux pécédentes en les soustrayant
- remplacer la valeur de la variable nom par celle de nom complet puis supprimer la variable nom complet

## Les types primitifs de variable
""")

code = """
# Les "integers", ou nombres entiers en français
nombre_apprentants = 7
print(type(nombre_apprentants),nombre_apprentants)
# <class 'int'> 7
"""
st.code(code, language='python')



code = """
# Les "floats", ou nombres à virgule en français
age_moyen_promo = 25.0
print(type(age_moyen_promo), age_moyen_promo)
# <class 'float'>25.0
"""
st.code(code, language='python')


code = """
# Les "strings" (str), ou chaines de caractères en français
apprenant = "Charles"
print(type(apprenant), apprenant)
# La variable apprennant est de type <class 'str'> et prend comme valeur Charles
"""
st.code(code, language='python')



code = """
# Les "Booléens" (bool), ou booléen en français, c'est à dire vrai ou faux
est_ce_que_1_plus_1_egale_2 = 1 + 1 == 2

print(type(est_ce_que_1_plus_1_egale_2),est_ce_que_1_plus_1_egale_2)
# <class 'bool'> True
"""
st.code(code, language='python')


st.markdown("""
## Les integers et les floats en détail 
### Opérations sur les integers et les floats

""")

code = """
x = 12.5
y = 3

#la somme de x et y (x plus y).
somme = x + y   
print (f"{somme=}") # somme=15.5

#la différence entre x et y 
difference = x - y 
print (f"{difference=}") # difference=9.5

#le produit de x et y
produit = x * y 
print (f"{produit=}") # produit=37.5

# le quotient de x et y (x divisé par y).
quotient = x / y 
print (f"{quotient=}") # quotient=4.166666666666667

# le quotient de x et y sans reste.
quotient_sans_reste = x // y 
print (f"{quotient_sans_reste=}") # quotient_sans_reste=4.0

# le reste de x divisé par y.
reste = x % y  
print (f"{reste=}") # reste=0.5

# x à la puissance y
puissance = x**y
print (f"{puissance=}") # puissance=1953.125
"""

st.code(code, language='python')

st.markdown("""

### fonctions utiles liées aux integers ou aux float 
""")
code = '''
# Valeur absolue de x
abs(x)

# obtenir l'arrondi d'un float
round(x,(nb_digits))

# Convert an object to integer
s = "8"
s_as_an_integer = int(s)

# Convert an object to float

s_as_a_float = float(s)
'''
st.code(code, language='python')

st.markdown("""
PLus de méthodes dans la documentation: https://docs.python.org/3/library/stdtypes.html

## Les strings en détail
### Les astuces concernant les strings
""")

code = '''
# Pour utiliser le symbole ` dans une string il faut écrire \``	
a_string = "J'aime \"le\" Python!"
print(a_string) # J'aime "le" Python!
a_string = "comme dit le poète \"slkdfnsklfdn\"" # comme dit le poète "slkdfnsklfdn" J'aime 

# Pour sauter une ligne \n
a_string_with_a_space =	"a line \n to an another"

print(a_string, the_same_string, a_string_with_a_space) 
#a line 
#  to an another
'''

st.code(code, language='python')

st.markdown("""
### Le parcours des chaines de caractères

""")

code = """
n = 2
the_string = "string"

# Renvoie le n ème élément d'une liste 
print(the_string[n])   # s

"""
st.code(code, language='python')

st.markdown("""### fonctions utiles"""
)

code = """
# Renvoie le nombre de caractère dans la string
len(the_string)

"""
st.code(code, language='python')


st.markdown("""
### Les méthodes de la classe str
"""
)

code = """
my_string = "Quelle belle journée belle journée"

# Mettre tout en minuscule
lower_string = my_string.lower()

# Mettre tout en majuscule
upper_string = my_string.upper()

# Mettre une majuscule au début
capitalized_string = my_string.capitalize()

# Remplacez une expression
replaced_string = my_string.replace("journée", "soirée")

# Cherchez un bout de la chaine
emplacement_de_belle = my_string.find("belle")

# Compte le nombre de fois ou apparait un caractère
count_string = my_string.count("l")

# Diviser une chaine de caractères pour créer une liste
splited_string = my_string.split(" ")

# Remplace les {} par la valeur définie dans format
my_string = "Quelle {} et {} journée".format("belle", "bonne")
my_string = "Quelle {adjectif_1} et {adjectif_2} journée".format(adjectif_2="belle", adjectif_1="bonne")



print("my_string :", my_string)
print(f"{my_string=}")
# my_string : Quelle bonne et belle journée
# Quelle bonne et belle journée
"""
st.code(code, language='python')


st.markdown("""
## Les booléens en détail
""")
code = """
x = 8
y = 9
z = [7 ,8 ]

\"\"\"Les booléens sont souvent le résultat d'une comparaison \"\"\"

print( x == y ) #equal

print( x != y ) # not equal

print( x < y ) #strictly less than

print( x <= y ) #less than or equal

print( x > y ) #strictly greater than

print( x >= y ) #greater than or equal

\"\"\" ou le résultat d'affirmation \"\"\"

print( type(x) is int ) # être

print( type(x) is not str ) # ou ne pas être

print (isinstance(x,str))  # Check if x is an String       Ex : isinstance(object, type)

print( x in z) # appartenir

print( y not in z ) # ou ne pas appartenir

\"\"\" enfin ils peuvent être combiné grâve à des opérateurs logique \"\"\"
t = True
f = False

print( t and f) # s'écrit aussi &
print( t or f) # s'écrit aussi | 
print( not t)
print( not f)
"""

st.code(code, language='python')



code = """
if 1:    ## Or 2, or 5, or 55465464 ... alaways true but but not 0
  print("hello")

# The same 
if "dfgdfg":    ## Always true for any charachter but not ""
  print("hello")
"""


st.code(code, language='python')