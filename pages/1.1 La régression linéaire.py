import streamlit as st
import pandas as pd

st.set_page_config(
    page_icon=":snake:",
)
st.markdown("<h1 style='text-align: center; color: black;'>La régression linéaire</h1>", unsafe_allow_html=True)

st.image("https://miro.medium.com/max/1200/0*MkEov3K6UUjhuwOd.jpeg")

st.markdown("Ce chapitre introduit la notion de modèle linéaire par la version la plus élémentaire : _**expliquer $Y$ par une fonction affine de $X$**_.")

st.markdown("""
# La régression linéaire
La régression linéaire est simple lorsque le modèle ne comporte qu'une variable explicative_ $X$.
##### Exemple : Prédire le prix du loyer d'un logement :
""")
d = {'Taille en m² (X)': [25, 35, 55, 44,23 ,27 ], 'Prix en 1000€ (Y)': [380, 423, 689, 254, 265, 234 ]}
df = pd.DataFrame(d)
st.dataframe(df)

st.markdown("""
Notons : 
- $X$ pour la taille du logement, c'est la **variable explicative** (feature)
- $Y$ pour le Prix en €, c'est la **variable à expliquer** (cible ou target)
- $m$ pour le nombre d'exemples (logements) d'entraînement (training examples)
- $n$ pour lr nombre de variables
- Une paire $(x^{(i)},y^{(i)})$ est appelée **training example**
- l'ensemble de données que nous allons utiliser $${(x^{(i)},y^{(i)}), i = 1,2,3,...}$$ (une liste de $m$ exemples de raining examples) est appelé un **training set**

### Qu'est-ce qu'une modélisation ?
C'est un algorithme qui lie une variable explicative (surface en $m^2$) par une variable à expliquer (le prix en €). Dans notre cas, notre algorithme est une fonction mathématique $h$.
La fonction $h$ s'appelle une **hypothèse**

Lorsque la variable cible que nous essayons de prédire est continue, comme dans notre exemple de logement,
 nous appelons le problème d'apprentissage un problème de **régression**. 
 Lorsque y ne peut prendre qu'un petit nombre de valeurs discrètes (comme si, compte tenu de la surface habitable, nous 
 voulions prédire si un logement est une maison ou un appartement, par exemple), nous appelons cela un problème de **classification**.
""")
st.image("LR1.png")

