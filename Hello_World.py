# https://blog.streamlit.io/introducing-multipage-apps/

# Contents of ~/my_app/streamlit_app.py
import streamlit as st

st.markdown("""
# Introduction à Python
""")


st.image(
            "https://thetechrim.com/wp-content/uploads/2018/10/Python_logo.png",
            #width=400, # Manually Adjust the width of the image as per requirement
        )
st.markdown("""
## Créer et lancer des programmes
Il existe de deux types de fichier pour créer des programmes en python:
- **Les fichiers scripts .py** : Ils sont légers et on peut facilement importer le contenu d'un script dans un autre script, on s'en servirra quand on développera des programes complexes qu'on voudra diviser en plusieurs fichiers comme par exemple des applications web
- **Les notebooks .ipynb** (comme ce fichier): ils permettent d'afficher directement le code utilisé, d'ajouter des commentaires complexes (titres, images, liens...). Ils sont très utilisés quand on veut explorer une base de données ou quand on veut expliquer quelque chose en intégrant du code. 

### Les fichiers scripts
Il suffit de créer un nouveau fichier, de lui donner un nom et d'ajouter .py à la fin (appelons le hello.py)

On va pouvoir écrire notre premier programme à l'intérieur. 

""")

code = """
print("Hello World")

print("This is my first python program")
"""
st.code(code, language='python')

st.markdown("""
On décomposera plus tard ce code, on va se contenter de le lancer en appuyant sur la flèche.
Cela lance un terminal (ou une console) où on voit apparaitre ce qu'on voulait voir apparaitre.

On a également souvent l'habitude de lancer le code directement depuis le terminal à l'aide de la commande suivante:
""")

code = """
"python3 hello.py"
"""
st.code(code, language='python')



st.markdown("""
### Les notebooks
#### Lancer un programme

Faisons la même chose avec un notebook.

Créons un fichier appelé hello.ipynb

Un notebook est divisé en cellules. Les cellules peuvent être lancées individuellement mais partagent le même environnement (on verra plus tard quand on parlera des variables par exemple que si on déclare une variable dans une cellule, on peut y accéder dans les autres cellules)

Dans la première cellule on peut écrire print("Hello World")

On va écrire le même programme et le lancer à l'aide de la flèche qui se trouve en haut à gauche de la cellule (print(Hello Word))
""")

code = """
print("Hello World")
"""

st.code(code, language='python')


st.markdown("""
On peut également la lancer avec le raccourci CTRL + Entrer. Les raccourcis sont très utilisés dans les notebooks ( [voir liste des raccourcis](https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330))

Pour bien les maitriser il faut comprendre la différence entre:
- **Le mode "edit"** : où on va écrire du code et le lancer (Quand on est sur une cellule, il faut appuyer sur entrer pour passer en mode "edit", c'est la même chose que de cliquer dans une cellule)
- **Le mode "action"** (ou commande): permet de gérer les cellules (Quand on est dans une cellule, appuyer sur echap pour passer en mode action)

#### Les raccourcis
Les raccourcis les plus utiles à mon gout:
- Les deux modes confondus:
    - Ctrl + Enter: lance la ou les cellules selectionnées
    - Ctrl + S: enregistre 
    - Ctrl + F: permet de faire un ctrl F 
- En mode "Edit":
    - Esc: passe en mode action
    - Ctrl + A: sélectionne toute la cellule
    - Ctrl + Z: supprime ce qu'on vient de faire
    - Ctrl + shift + Z: remet ce qu'on vient de supprimer   
- En mode "Action":
    - Enter: passe en mode Edit
    - A: insert une cellule au dessus
    - B: insert une cellule en dessous
    - X: coupe une cellule (qu'on peut utiliser aussi pour la supprimer sinon deux fois D)
    - C: copie une cellule 
    - V: colle une cellule
    - Y: transforme une cellule Markdown en cellule Code 
    - M: transforme une cellule Code en cellule Markdown

Il existe en effet deux types de cellule:
- Les cellules Code: pour écrire et lancer du code
- Les cellules Markdown: pour écrire des commentaires, des titres, ajouter des liens ou des images

`Exercice`: 
- Créer une cellule en dessous
- Ecrivez print("This is my first python program")
- Transformer cette cellule en Markdown puis de nouveau en code puis exécutez la (lancez la)
- Créer une cellule Markdown puis ajouter le commentaire "Dans un notebook, les cellules se lancent indépendamment 

#### Les markdows en détails

On peut créer différentes choses:
- des puces
- par exemple
    - et des sous-puces naturellement

Mettre des choses en `évidence` ou en **gras**, voire *en italique* 

Créer des liens: [le lien](https://en.wikipedia.org/wiki/Python_(programming_language))

<font color="red"> Changer de couleur en s'inspirant de HTML </font>


Et insérer des images

""")

code = """
![image](https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg)
"""
st.code(code, language='markdown')

st.image("https://interactive-examples.mdn.mozilla.net/media/cc0-images/grapefruit-slice-332-332.jpg")

