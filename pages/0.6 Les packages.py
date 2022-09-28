import streamlit as st




st.image("https://blog.engineering.publicissapient.fr/wp-content/uploads/2020/09/python.jpg")


st.markdown("""
# Importation: packages et fichiers
## Présentation des packages
Un package est un fichier ou un ensemble de fichiers qui contient des fonctions et des classes qui peuvent être réutilisés dans d'autres programmes

## Importer un package dans son environnement de dev depuis votre librairie de package
Pour utiliser un package il faut l'importer depuis votre librairie de package.  
Celle-ci est constituée par python et par anaconda  
""")
code = """
# exemple d'utilisation
import math 

x = 5.8999
print( math.floor(x))
"""
st.code(code,language="python")




code = """
# en utilisant import math on est obligé de préciser le nom du package:
floor(5.8999)
"""
st.code(code,language="python")



code = """
''' il existe trois manières d'importer un package: deux légales et une illégale '''
# LEGAL: importer tout un package en s'obligeant en indiquant le nom du package avant:
import math as math
x = math.floor(5.899999)


# LEGAL: importer une partie d'un package sans devoir indiquer le nom du package avant de s'en servir:
from random import randint
y = randint(0,10)
print(y)

# ILLEGAL: importer tout un package sans devoir indiquer le nom du package avant de s'en servir:
from random import *
z = uniform(0,1)
print(z)
"""
st.code(code,language="python")



st.markdown("""
## Installer un package dans sa librairie de package puis l'importer

Vous pouvez trouver des packages qui ne sont ni dans python ni anaconda
""")
code = """
import pandas
"""
st.code(code,language="python")



st.markdown("""
Vous devez auparavant installer ce package dans votre librairie de package à l'aide de la commande:
- **`pip3 install pandas`**

Cette commande doit être tapée dans votre terminal
""")
code = """
# vous pouvez ensuite l'importer dans votre environnement de dev
import pip
"""
st.code(code,language="python")



st.markdown("""
Autres commandes utiles:
- pip show <package(s)>
- pip list
- pip freeze

## Se servir d'un package

Pour connaitre comment se servir d'un package vous pouvez procéder en deux temps

D'abord obtenir la liste des objets et fonctions dans ce package


""")
code = """
dir(math)
"""
st.code(code,language="python")




st.markdown("""
ensuite demander l'aide sur une fonction particulière
""")
code = """
help(math.tan)
"""
st.code(code,language="python")





st.markdown("""
# Les environnements virtuels

Un environnement virtuel est un dossier qui regroupe une certaine version de python et ainsi que certains packages et leurs versions propres à un projet. Le projet sera exécuté au sein de cet environnement.
Cela permet:
- de garder un environnement léger: savoir quel package il faut installer quand on clone un nouveau projet et non tous les packages de l'ordinateur de la personne qui a créé le projet
- connaître la version des packages et des dépendances où le projet fonctionne (des mises à jour peuvent rendre un projet inutilisable)


Il existe de nombreux outils de gestion d'environnement virtuel:
- venv: inclus dans python
- virtualenv: le plus ancien, permet de gérer des version de python 2
- conda: qui vient avec anaconda
- Pipenv: la solution en vue, qui regroupe pip et virtualenv


Nous allons voir venv, ce n'est pas le plus recommandé pour des usages complexes mais il a l'avantage d'être inclu dans python.


Les commandes qu'il faut connaitre (à taper dans le terminal):
- **`python -m venv env`** : crée un environnement appelé env
- **`source env/bin/activate`** (Unix) ou **`..\env\Scripts\activate`** (WIndows): active l'environnement virtuel: à partir de maintenant quand on lance un fichier depuis le terminal ou qu'on install un package avec pip, ce sera dans cet environnement
- **`deactivate`** : désactive l'environnement
- **`rm -rf env`** : supprimer l'environnement virtuel
- **`pip freeze > requirements.txt`** : crée un fichier requirements.txt avec tous les packages du projet et leur version
- **`pip install -r requirements.txt`** : install tous les packages fu fichier requirement

Article médium sur l'équivalent en [Pipenv](https://medium.com/analytics-vidhya/why-pipenv-over-venv-for-python-projects-a51fb6e4f31e) et l'interet d'utiliser ce package

## Importer des fichiers et des packages qu'on a soit même créé.
Il existe une bonne pratique chez les développeurs de créer leurs classes et leurs fonctions dans des fichiers séparés (normalement une classe ou une fonction par fichier). Pour pouvoir faire cela il faut pouvoir importer un fichier.


""")
code = """
# il est assez facile d'importer une fonction du même niveau

from Same_level import same_level_function
same_level_function("Same")
'''
this is a function from a same level file
this is a function from a same level file
'''
"""
st.code(code,language="python")









st.markdown("""

""")
code = """
# De même pour un fichier enfant

from child_folder.child_file import child_file_function
child_file_function()
'''
I'm a child file function
I'm a child file function
'''
"""
st.code(code,language="python")



code = """
import sys
from pprint import pprint
pprint(sys.path)
"""
st.code(code,language="python")



st.markdown("""
Dans l'autre sens ça se complique un peu ...
""")

st.image("https://thefnublogen.files.wordpress.com/2018/11/complicated.png")

code = """
import os
import sys
import inspect

# Importation d'un fichier depuis un fichier parents

# je recherche dans un premier temps le chemin de mon répertoire courant
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# A partir de celui-ci je déduis le chemin de mon répertoire parent
parentdir = os.path.dirname(currentdir)

# J'ajoute le chemin de mon répertoire parent au "python path" 
# qui est l'endroit ou la fonction import va chercher ce qu'elle est capable d'importer
sys.path.insert(0, parentdir) 

from pprint import pprint
#pprint(sys.path)

import Same_level
print(Same_level.same_level_function("Child"))


# Importtion d'un fichier depuis un fichier brother

# de nouveau je dois trouver le chemin
brotherdir = os.path.join(parentdir, "other_folder")

# puis l'ajouter au python path
sys.path.insert(0, brotherdir)

import other_folder_file 
print(other_folder_file.other_folder_function())
"""

st.code(code, language="python")