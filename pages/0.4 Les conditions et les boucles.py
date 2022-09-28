from re import L
import streamlit as st




st.image("https://user.oc-static.com/upload/2021/12/09/1639058458628_P1C6_Structurez-votre-code-a%CC%80-laide-des-conditions.png")







st.markdown("""
# Les conditions
""")
code = """
\"\"\" Structure générale d'une condition if \"\"\"
if mon_booleen:
   # exécuter le code quand mon_booleen est vrai
else:
   # exécuter le code quand mon_booleen est faux
"""
st.code(code,language="python")



st.markdown("""
Rappel: Les booléens peuvent être combinés avec des opérateurs logiques (and, or ..) ou issus de comparaisons (<, >, == ...)
""")
code = """
''' Exemple '''

ensoleille = False

if ensoleille:
   print("on va à la plage !")
else:
   print("on reste à la maison !")
# on reste à la maison !
"""
st.code(code,language="python")




code = """
''' Il est également possible d'ajouter d'autres conditions '''

ensoleille = False
neige = True

if ensoleille:
   print("on va à la plage !")
elif neige:
   print("on fait un bonhomme de neige")
else:
   print("on reste à la maison !")

a = 8

if a > 2:
   print(a)
if a < 7:
   print(a)
else:
   print("nothing")


"""
st.code(code,language="python")



st.image("https://blog.4d.com/wp-content/uploads/2018/01/ForEach720.png")

st.markdown("""
## La boucle for
""")
code = """
#Le principal interet de la boucle for est de parcourir des listes
liste_apprenants = ["Pascal", "Azel", "Tony", "Vladimir", "Sabrina"]

for element in liste_apprenants:
    print(element, " présent")
   '''
   Pascal  présent
Azel  présent
Tony  présent
Vladimir  présent
Sabrina  présent
   '''
"""
st.code(code,language="python")




st.markdown("""
On peut également s'en servir avec la fonction range, cela permet de parcourir une liste d'entiers
""")
code = """
print(type(range(5)))
print(range(5))

'''
<class 'range'>
range(0, 5)
'''


for i in range(10):
    print(i)

'''
2
4
6
8
'''
"""
st.code(code,language="python")


code = """
# la fonction range peut prendre plusieurs arguments:
premier_element = 2
dernier_element_plus_1 = 11
pas = 2 # on compte tous les combien

for j in range(premier_element,dernier_element_plus_1,pas):
    print(f"j = {j}")

premier_element = 11
dernier_element_plus_1 = 7
pas = -3 # on compte tous les combien

for k in range(premier_element,dernier_element_plus_1,pas):
    print(f"k = {k}")   

'''
j = 2
j = 4
j = 6
j = 8
j = 10
k = 11
k = 8
'''
"""





st.markdown("""
## Boucle While
""")
code = """
# La structure générale de la boucle while est la suivante:

i = 0
condition = 10 > i

while condition:
    print(f"la condition est encore vraie car i vaut {i}")
    i += 1 # on appelle cela l'incrementation
    condition = 10 > i

'''
la condition est encore vraie car i vaut 0
la condition est encore vraie car i vaut 1
la condition est encore vraie car i vaut 2
la condition est encore vraie car i vaut 3
la condition est encore vraie car i vaut 4
la condition est encore vraie car i vaut 5
la condition est encore vraie car i vaut 6
la condition est encore vraie car i vaut 7
la condition est encore vraie car i vaut 8
la condition est encore vraie car i vaut 9
'''
"""
st.code(code,language="python")


code = """
# l'incrémentation permet de ne pas créer de boucle infinie
i=11
condition = 12 > i
while condition:
    print("ceci est une boucle infinie")
    
"""
st.code(code,language="python")

