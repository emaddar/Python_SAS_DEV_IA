import streamlit as st


st.set_page_config(
    page_icon=":snake:",
)
st.markdown("<h1 style='text-align: center; color: black;'>Les fonctions</h1>", unsafe_allow_html=True)


st.image("https://accromath.uqam.ca/wp-content/uploads/2013/08/fonctions_titre.png")


st.markdown("""
# Les fonctions
""")
code = """
Une fonction est un bloc de code avec un but spécifique auquel vous pouvez donner un nom. 
- Elles sont dans un premier temps définies 
- Puis exécuter. 
Quand vous appelez une fonction, vous exécutez le code qu’elle contient. Les fonctions vous laissent saisir des paramètres pour exécuter le même code sur différentes valeurs.
"""
st.code(code,language="python")


















st.markdown("""
## Les fonctions de base
""")
code = """
Certaines fonctions sont déja définies dans python, on en a déja rencontré quelques unes:
- len(x)
- type(x)
- max(x)
"""
st.code(code,language="python")





st.markdown("""
Pour savoir à quoi sert une fonction (ou une classe) il existe une autre fonction:
""")
code = """
help(max)
'''
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
'''
"""
st.code(code,language="python")













st.markdown("""
Pour les autres fonctions built-in : https://docs.python.org/3/library/functions.html#help

## Définir une fonction

Il est également possible de créer ses propres fonctions
""")
code = """
''' Structure générale d'une fonction '''

# étape de la définition
def fonction_name(parametre_1,parametre_2):
    #instructions
    return result

# étape de l'appel
resultat = fonction_name("quelque_chose","autre_chose")
"""
st.code(code,language="python")



code = """
'''Exemple'''

def add(a,b):
    return a+b

print(add(3,4))
"""

st.code(code,language="python")














st.markdown("""
## Docstring
Selon la PEP 8, chaque partie de votre code devrait contenir une Docstring.
- tous les modules publics
- toutes les fonctions
- toutes les classes
- toutes les méthodes de ces classes
""")
code = """
def add(a,b):
    '''
    This function returns the sum of the two parameters

    parameters
    ----------
    a: int
    b: int
    '''
    aprime = abs(a)  # on prend la valeur absolue
    bprime = abs(b)  
    return a + b
"""
st.code(code,language="python")


code = """
help(add)
'''
Help on function add in module __main__:

add(a, b)
    This fonction returns the sum of the two parameters
    
    parameters
    ----------
    a: int
    b: int
'''
"""
st.code(code,language="python")

















st.markdown("""
Cependant la Pep 8 nous demande également d'être concis dans nos commentaires et de ne pas commenter des évidences. Il faut donc se poser la question de savoir si ce que nous écrivons est évident pour quelqu'un qui n'a pas écrit le code (ici oui), si ce n'est pas évident alors il faut commenter

**`règles d'écriture`**:
- fonctions: minuscules et tiret du bas : my_function()
- arguments des méthodes et fonctions : identique aux fonctions. my_function(param=False)  (attention pas d'espace)



## Fonctions et Méthodes

Les fonctions et les méthodes sont des objets proches mais qui possèdent des différences et donc ne doivent pas être confondus:
- Une fonction est défninie independement de tous objets, les objets auxquels elle s'applique sont tous précisés dans ses paramètres
    - **exemple**: round(un_float,2), sum(une_liste), sum(un_int, autre_int)...
- Une méthode est liée à une classe d'objet, elle est définie au moment de la défnition de la classe. On applique toujours une méthode à une instance de classe. Comme on appelle la méthode à partir de cette instance, on ne la rappelle pas dans les paramètres:
    - **exemple**: une_instance_str.upper(), une_instance_liste.append(3)
""")
code = """

"""
st.code(code,language="python")