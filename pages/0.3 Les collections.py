import streamlit as st
st.image("http://www.aftenposteninnsikt.no/sites/default/files/styles/preset_1_article_carousel_image/public/web_iStock-860844068.jpg?itok=2-RmQfWr")
st.markdown("""
# Les listes 
## définition et déclaration
Une liste est une collection d'objets:
- dont l'ordre compte, elle est ordonnée (contrairement aux dictionnaires et aux sets) 
- dont les éléments peuvent être modifiés (contrairement aux tuples et aux sets)
- dont un élément peut être répétés plusieurs fois (contrairement aux sets)
""")

code = """
# Créer des listes contenants des éléments:
liste_de_nombres = [1, 2, 3, 5, 7, 11, 13, 17,17]
liste_de_strings = ["a", "b", "abc"]
liste_foutoire = [7, 4.2, "un truc", True, ["une","autre","liste"]]

# Créer des listes vides: 
liste_vide = []
liste_vide = list()
"""
st.code(code, language="python")


























st.markdown("""
## On accède aux éléments d'une liste par leur indice
""")

code = """
# On accède aux éléments d'une liste ainsi:
# soit en partant du début
#    le premier élément se trouve à l'indice 0
print(liste_de_nombres[0], " est le 1er élément")
print(liste_de_nombres[4], " est le 5ème élément") 

# soit par la fin
print(liste_de_nombres[-1], " est le dernier élément")

# On peut supprimer un élément en se servant de son indice
#del liste_foutoire[3]

# On peut également selectionner une partie de la liste
liste_de_nombres[1:3]

# On peut également  selectionner tous les premiers ou tous les derniers éléments
liste_de_nombres[:3]
liste_de_nombres[3:]
liste_de_nombres[3:-2]

liste_foutoire[4][1][2] # C'est pour chercher l'indice 1 dans l'indice 4 (car dans cette liste, il y a une liste), ensuite chercher la charachter n. 3 (indice 2)
"""
st.code(code, language="python")


code = """
# On peut ainsi modifier les valeurs d'une liste à un certain indice
liste_de_nombres[3] = 8


# delete indice 3
del liste_de_nombres[3]
"""

st.code(code, language="python")


code = """
#Obtenir une liste en sens inverse
liste_de_nombres[4::-1]
# [11, 7, 3, 2, 1]
"""

st.code(code, language="python")





st.markdown("""
## fonctions utiles
""")

code = """
# connaitre le nombre d'éléments dans une liste
len(liste_de_nombres)

# connaitre la somme d'une liste numérique
sum(liste_de_nombres)

# connaitre le maximum ou le minimum d'une liste numérique
max(liste_de_nombres)
min(liste_de_nombres)

# connaitre tous les élements uniques
set(liste_de_nombres)
# [('Netflix', 198), ('Hulu', 166), ('Sling', 237), ('Hbo', 125)]
"""
st.code(code, language="python")














st.markdown("""
## Méthodes associées à la classe liste
""")

code = """
# ajouter un élément à la fin une liste
liste_de_nombres.append(89)

# Ajoute un élément à une liste à une certaine position (ici au début: 0)
liste_de_nombres.insert(0, -1) # d'abord l'indice puis ce qu'on ajoute

# concatène deux listes (ajoute une liste à une autre)
liste_de_nombres.extend(liste2)  # or we can use : list1 + list2

# supprimer un élément d'une liste
liste_de_strings.remove("abc") # this will remove the first "abs"

# supprime le dernier élément d'une liste
liste_de_strings.pop() # this will delete  the laste element
liste_de_strings.pop(0) # this will remove the first one

# ordonner les éléments d'une liste
liste_de_nombres.sort(reverse=True)

# retrouve l'indice de la première occurrence d'un élément à chercher dans notre liste ;
liste_de_nombres.index(5)

# savoir si une liste est une sous liste d'une autre
set(liste2).issubset(liste_de_nombres)
"""
st.code(code, language="python")


st.markdown(""" Pour les autres méthodes voir la : https://docs.python.org/fr/3/tutorial/datastructures.html """)


code = """
liste_nombres = [1, 6, 98, 52, 1045, 3]

# 1) classez la liste en ordre croissant
liste_nombres.sort()
liste_nombres

# 2) supprimez le premier élément de la liste
liste_nombres.pop(0)
liste_nombres

# 3) ajoutez le nombre "1097" à la fin de la liste
liste_nombres.append(1097)

# 4) récupérez le deuxième élément dans une variable "deuxieme_element"
deuxieme_element = liste_nombres[1]
# print(deuxieme_element) # la console devrait afficher "6" !
deuxieme_element
# 5) affichez la longueur de la liste
print(len(liste_nombres))


"""
st.code(code, language="python")



st.markdown("""
# Les dictionnaires
## Définition et création
Un dictionnaire est un objet permettant de stocker des informations à l'aide d'un système clé/valeur.
A chaque clé correspond une valeur, les clés n'ont pas d'odre entre elles.

### Créer un dictionnaire vide
""")
code = """
new_dict={}
new_dict = dict()
print(new_dict)
"""
st.code(code, language="python")




st.markdown("""
### Créer un dictionnaire contenant des données
""")
code = """
trucs_appris_en_python = { 
    "lesstrings": "exemple", 
    "lesintegers": 9, 
    "leslistes": [7,8,9], 
    "les booleen": True 
}

print(trucs_appris_en_python)
# {'lesstrings': 'exemple', 'lesintegers': 9, 'leslistes': [7, 8, 9], 'les booleen': True}
"""
st.code(code, language="python")



st.markdown("""
Restriction:
- Les clés peuvent être des int, des float, des str (tout object immutable (voir plus loin)) mais une clé ne peut être utilisée qu'une seule fois 
- les valeurs peuvent être ne n'importe quel type

## Accéder aux valeurs
""")
code = """
# Accéder à une valeur à partir de sa clé
trucs_appris_en_python["lesstrings"]


# On peut à tout moment ajouter une nouvelle clé à un dictionnaire en lui attribuant une valeur
trucs_appris_en_python['lesfloats'] = 3.8
trucs_appris_en_python
'''
{'lesstrings': 'exemple',
 'lesintegers': 9,
 'leslistes': [7, 8, 9],
 'les booleen': True,
 'lesfloats': 3.8}
'''


# On modifie la valeur comme on modifierait une variable
trucs_appris_en_python['lesfloats'] = 3.9


# supprimer un couple clef/valeur
del trucs_appris_en_python['lesfloats']
print(trucs_appris_en_python)

# une autre manière de supprimer un couple cle/valeur:
trucs_appris_en_python.pop('lesstrings') 
trucs_appris_en_python
'''
{'instagram': 1.8}
{'lesstrings': 'exemple',
 'lesintegers': 9,
 'leslistes': [7, 8, 9],
 'les booleen': True}
'''


"""
st.code(code, language="python")


st.markdown(""" ## Parcourir un dictionnaire """)
code = """
# vérifier l'existence d'une clef:
print("leslistes" in trucs_appris_en_python)
# True
# True

# trois méthodes importantes liées aux dictionnaires:
print(trucs_appris_en_python.keys())
print(trucs_appris_en_python.values())
print(trucs_appris_en_python.items())
'''
dict_keys(['lesstrings', 'lesintegers', 'leslistes', 'les booleen'])
dict_values(['exemple', 9, [7, 8, 9], True])
dict_items([('lesstrings', 'exemple'), ('lesintegers', 9), ('leslistes', [7, 8, 9]), ('les booleen', True)])
'''

# Utilisation de values()
print( 9 in trucs_appris_en_python.values() )


# Utilisation de items()
print( ("lesintegers",9) in trucs_appris_en_python.items() )

"""
st.code(code, language="python")

st.markdown(""" 
# La Mutabilité
## Définition
Observons quelque chose:

""")

code = """

a = "Charles"

a.upper()

print(a) # Charles


b = [1,2]

b.append(3)

print(b) # [1, 2, 3]
"""
st.code(code, language="python")

st.markdown("""
Quand on définit une variable en python on définit toujours un nom qui pointe vers une valeur enregistrée en mémoire. En fonction du type d'objet la valeur inscrite en mémoire peut être modifiée ou non. On appelle cela la mutabilité
- Les Objets immutables sont ceux dont la valeur en mémoire ne peut changer: Entiers, flottants, complexes, tuples, chaînes de caractères, …
- LEs Objets mutables sont ceux dont la valeur en mémoire change: Listes, dictionnaires, …

## Récupérer le résultat des opétations 
Quand on modifie un object immutable, ce que l'on fait en réalité c'est de déclarer une nouvelle valeur en mémoire. Cette nouvelle valeur si on veut s'en servir il faut lui donner un nouveau nom et donc l'assigner à une variable

Pour les object mutable, quand on les modifie, c'est directement l'objet en mémoire qui est modifié, pas besoin donc d'assigner un nouveau nom de variable pour ce résultat. Si on le fait, python n'enregistrera pas la nouvelle valeur prise mais un objet nul ou parfois le résultat de l'opération. C'est donc le meilleur moyen de perdre ses données:

""")


code = """
a = "Charles"

a_bis = a.upper()

print(a_bis)

a = a.upper()

print(a)


b = [1,2]

b_bis = b.append(3)

print(b_bis)

b = b.append(3)

print(b)

"""
st.code(code, language="python")


st.markdown("""

## Créer des alias et des copies
On peut faire en sorte qu'une variable soit égale à la valeur d'une autre variable
""")
code = """
a = "Charles"
b = [1,2]

a_alias = a
b_alias = b
"""
st.code(code, language="python")

st.markdown("""
Dans ce cas là, on crée en réalité un alias, on crée un nouveau nom qui point vers la même valeur en mémoire.
On a vue que pour les immutables, la valeur en mémoire ne changeait pas, si on fait donc pointer l'un des deux alias vers une nouvelle valeur, l'autre pointera toujours vers l'ancienne valeur inchangée
""")
code = """
a = a.upper()
print(a)
print(a_alias)
'''
CHARLES
Charles
'''
"""
st.code(code, language="python")

st.markdown("""
Pour les objets mutables, c'est la valeur en mémoire qui change. Si donc on la modifie en utilisant un des deux alias, l'autre alias pointera égaement vers la valeur modifiée
""")
code = """
b.append(3)
print(b)
print(b_alias)
'''
[1, 2, 3]
[1, 2, 3]
'''
"""
st.code(code, language="python")

st.markdown("""
Si on veut conserver l'état initial d'un objet mutable, il ne faut pas créer un alias mais une copie
""")
code = """
b_copie = b.copy()


b.append(4)

print(b)
print(b_copie)
'''
[1, 2, 3, 4]
[1, 2, 3]
'''
"""

st.code(code, language="python")


st.markdown("""
**`Exercice`**: 

- Déclarer une variable de type float égale à 3.9874. 
    - Conserver une copie de cette état initial
    - Calculer la valeur absolue de cette variable. 
    - Puis ajouter cette valeur absolue à la valeur initiale de la variable 
    - (Toutes ces étapes sont à faire sépérement et pas sur une seule ligne)
- Créer un dictionnaire avec une cle "nombre" et comme valeur l'int 90
    - Conserver une copie de cette état initial
    - Modifier la cle pour lui donner comme valeur 150
    - additionner les valeurs de cette clé pour l'état initial et l'état modifié


""")

code = """
variable_float = -3.9874
variable_float_copy = variable_float
abs(variable_float)
variable_float = abs(variable_float)

my_dicstionnaire = {"nombre":90}
my_dicstionnaire_copy = my_dicstionnaire.copy()
my_dicstionnaire['nombre'] = 150

print(my_dicstionnaire['nombre'])
print(my_dicstionnaire_copy['nombre'])
'''
150
90
'''
"""



