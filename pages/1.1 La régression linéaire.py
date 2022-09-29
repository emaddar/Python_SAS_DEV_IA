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
d = {'Taille en m² (X)': [55, 110, 60, 75,150  ], 'Prix en 1000€ (Y)': [195000, 305000, 205000, 280000, 370000]}
df = pd.DataFrame(d)


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(df)


st.markdown("""
Représentation graphique du prix d'appartements en fonction de la surface en m²
""")


st.markdown(r"""
Notons : 
- $X$ pour la taille du logement, c'est la **variable explicative** (feature)
- $Y$ pour le Prix en €, c'est la **variable à expliquer** (cible ou target)
- $m$ pour le nombre d'exemples (logements) d'entraînement (training examples)
- $n$ pour lr nombre de variables
- Une paire $(x^{(i)},y^{(i)})$ est appelée **training example**
- l'ensemble de données que nous allons utiliser $${(x^{(i)},y^{(i)}), i = 1,2,3,...}$$ (une liste de $m$ exemples de raining examples) est appelé un **training set**, Les variables de la $2$ème observation, par exemple, sont notées $x^{(2)} = 110$ et $y{(2)} = 305000$.

### Qu'est-ce qu'une modélisation ?
C'est un algorithme qui lie une variable explicative (surface en $m^2$) par une variable à expliquer (le prix en €). Dans notre cas, notre algorithme est une fonction mathématique $h$.
La fonction $h$ s'appelle une **hypothèse**
""")
st.image("LR1.png")

st.markdown(r"""
Lorsque la variable cible que nous essayons de prédire est continue, comme dans notre exemple de logement,
 nous appelons le problème d'apprentissage un problème de **régression**. 
 Lorsque y ne peut prendre qu'un petit nombre de valeurs discrètes (comme si, compte tenu de la surface habitable, nous 
 voulions prédire si un logement est une maison ou un appartement, par exemple), nous appelons cela un problème de **classification**.

### L'hypothèse 
est la fonction qui doit être apprise par l'algorithme d'apprentissage par la progression de la formation pour faire les prédictions sur 
les données invisibles. $h$ is given by :
$$
h_{\theta}(X) = \theta_0 + \theta_1 X
$$
où : $\theta_0$ et $\theta_1$ sont les paramètres de la régression linéaire simple qui doivent être estimés.
- $\theta_0$ est l'ordonnée à l'origine (intercept) et
- $\theta_0$ est la pente de la droite.

### Paramètres de l'hypothèse 

""")


