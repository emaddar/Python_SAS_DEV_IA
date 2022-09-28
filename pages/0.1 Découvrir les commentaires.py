import streamlit as st
st.image("https://waytolearnx.com/wp-content/uploads/2020/06/Les-commentaires-en-Python-1.jpg")
st.markdown("""
# Découvrir les commentaires
Nous avons vu que les markdowns permettaient de créer des commentaires, cependant ils ne sont pas accessibles dans les fichiers scripts et parfois on veut commenter différemment.
""")

code = """
# commentaire
# ligne
# à ligne

print(\"Nous sommes bien ici dans une cellule de code\") # un commentaire ligne à ligne peut se mettre ici

\"\"\" Commentaire 
multi ligne\"\"\"

print("Les commentaires ne s'affichent pas quand on lance le code")
"""

st.code(code, language="python")


st.markdown("""
Autre différence entre ces deux types de commentaires
- Les commentaires ligne à ligne ne sont pas lus par python, il faut donc les utiliser en général.
- Les commentaires multi ligne sont lus par python mais pas affichés sauf dans certaines foncitons. On s'en sert généralement pour décrire une fonction, une classe ou un package
""")

code = """
def f(x):
    \"\"\" cette fonction ajoute 1 à x\"\"\"
    # tu le savais ?
    if True:
        print(True)
    return x +1

help(f)
"""
st.code(code, language="python")

st.markdown("""
Enfin, on utilise souvent un raccourci qui permet de commenter ligne à ligne plusieurs lignes en même temps:  
Ctrl + SHIFT + / (sur les lignes selectionnées)


**`Exercice`**: 
- copier coller les règles de la pep 8 dans votre fichier script en tant que commentaire multiligne et ligne à ligne (essayez les raccourcis et relancer le script)
- copier coller les règles de la pep 8 dans une cellule code, faite le même exercice que précédemment puis copier coller dans un cellule markdown et faire une mise en page correcte

### Règles Pep8:

Pep 8 sur les commentaires.
Ecrivez des phrases complètes, ponctuées et compréhensibles.
Le commentaire doit être cohérent avec le code.
Il doit suivre la même indentation que le code qu'il commente.
Evitez d'enfoncer des portes ouvertes : ne décrivez pas le code, expliquez plutôt à quoi il sert.
Il doit être en anglais.
""")

