import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)
from scipy import stats
import numpy as np

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

x = [55, 110, 60, 75,150  ]
y = [195000, 305000, 205000, 280000, 370000]

fig = plt.figure()
plt.scatter(x, y)
# plt.plot(x, y)
st.pyplot(fig)


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
\hat{y} = h_{\theta}(X) = \theta_0 + \theta_1 X
$$
où : 
- $\hat{Y}$ désigne la valeur prédite par le modèle, à la différence du $Y$ normal qui désigne la vraie valeur de la variable. L
- a fonction $h_{\theta}$ s'appelle la fonction de prédiction (ou d'hypothèse), et les valeurs $\theta_0$ et $\theta_1$ s'appellent les paramètres du modèle. On peut également considérer que le modèle a un seul paramètre $\theta$, qui est un vecteur de composantes $(\theta_0, \theta_1)$.
- $\theta_0$ est l'ordonnée à l'origine (intercept) et
- $\theta_0$ est la pente de la droite.
""")

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

fig = plt.figure()
plt.scatter(x, y)
plt.plot(x, mymodel)
st.pyplot(fig)

st.markdown(r"""
L'apprentissage consiste ici à déterminer quelles sont les valeurs de θ0 et θ1 qui donnent la meilleure estimation de $Y$. 
Concrètement, pour la représentation graphique, il s'agit de **tracer une droite qui s'approche la plus possible de toutes les observations**.


### La fonction coût : l’erreur quadratique moyenne
Pour préciser ce que signifie une “bonne estimation” de Y, on définit ce qu'on appelle une **fonction d'erreur** (**cost function**),
 qui mesure l'erreur entre les valeurs prédites par le modèle et les valeurs obervées. Dans la régression linéaire, on utilise la fonction
  d'erreur dite des **moindres carrés**, qui a la forme suivante:
$$
J(\theta_0, \theta_1) = \frac{1}{2m}\sum_{i=1}^m (h_{\theta}(x^{(i)}) - y^{(i)})^2
$$
Cette fonction représente la sommme sur toutes les observations de la distance (au carré) entre la valeur observée de $Y$ et sa valeur prédite par le modèle $h_{\theta}(x^{(i)})$.
Comme le but est que l'erreur (Distance entre les observations et les prédictions) soit globalement la plus petite possible, le problème revient à **minimiser** la fonction d'erreur $J$, 
c'est-à-dire à trouver le paramètre $\theta$ pour lequel la valeur $J(\theta_0,\theta_1)$ est minimale.
- Le terme m sert à faire la moyenne
- Le terme $\frac{1}{2}$ est ajouté comme une astuce afin de faciliter les calculs de la descente du gradient par la suite.

Cette fonction est appelée **Mean Squared Error (MSE)**, **Squared Error function** et en français on parlera plutôt de la **méthode des moindres carrés* (ou encore l'**erreur quadratique moyenne**)

Ce qu'il y a de fascinant, c'est que ce problème est résumé à un seul résultat, la valeur de la fonction coût. Si on minimise cette fonction coût, on trouvera les meilleurs paramètres $\theta$ et donc la modélisation la plus performante.


### Rappel : qu’est-ce que la dérivée d’une fonction ?
Graphiquement, la dérivée d'une fonction correspond à la pente de sa droite tangente
en un point spécifique.


Par exemple, voici le graphique d'une fonction, dessinée en noir, et une ligne tangente à cette fonction, dessinée en rouge. La pente de la tangente est égale à la dérivée de la fonction au point marqué.

""")
# \theta_j := \theta_j - \alpha\frac{\partial J}{\partial \theta_j}.
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Tangent_to_a_curve.svg/214px-Tangent_to_a_curve.svg.png")



st.markdown(r"""
### L’algorithme de descente du gradient
La méthode la plus simple pour minimiser la fonction d'erreur est l'algorithme de descente du gradient.
 Comme J est une fonction à 2 variables ($\theta_0$ et $\theta_1$), on peut la représenter en 3 dimensions par une surface d'équation
$z=J(X,Y)$.

L'idée de la méthode de descente du gradient est que pour trouver le minimum de la fonction $J$, 
c'est-à-dire le point le plus bas de la surface, il suffit de partir d'un point quelconque de cette surface et de la parcourir en prenant toujours
 la direction qui “descend” le plus rapidement possible, c'est-à-dire en avançant “face à la pente” de la surface (en réalité la méthode ne fonctionne
  à coup sûr que si la fonction n'a qu'un seul minimum local, ce qui est le cas de la fonction $J$).
""")

st.image("https://dridk.me/images/gradient_descendant/gradientDescent.jpg")


st.markdown(r"""
Mathématiquement, cette direction est donnée par le gradient de la fonction $J$, qui est le vecteur dont les composantes 
   sont les dérivées partielles de la fonction par rapport à chacune de ses variables:

   $$
\triangledown  J(\theta_0, \theta_1) = \binom{ \frac{\partial}{\partial \theta_0} J(\theta_0, \theta_1) }{ \frac{\partial}{\partial \theta_1} J(\theta_0, \theta_1) }   
   $$

L'algorithme consiste donc à choisir des valeurs initiales quelconques pour $\theta_0$ et $\theta_1$, et à ajuster ces paramètres de
 manière itérative en suivant la direction du gradient de $J$. Concrètement, on applique à chaque itération la formule suivante:

 $$
\left\{\begin{matrix}
\theta_0 =: \theta_0 - \alpha \frac{\partial}{\partial \theta_0} J(\theta_0, \theta_1) \\ 
\theta_1 =: \theta_1 - \alpha \frac{\partial}{\partial \theta_1} J(\theta_0, \theta_1)
\end{matrix}\right.
 $$


où $\alpha$ (hyper parameter) est appelé le **taux d'apprentissage** (**learning rate**). 

Il faut exécuter cette boucle jusqu'à la convergence de l'algorithme, c'est-à-dire jusqu'à ce que les paramètres $\theta_i$ ne varient (presque) plus.

#### Hyperparamètre : alpha
Alpha est un **hyperparamètre** qui est appelé le **coefficient d'apprentissage**. 

Un hyperparamètre, c'est un paramètre que l'algorithme ne peut pas apprendre par lui-même. Il faut tester l'algorithme en faisant varier cet hyperparamètre.

Plus le coefficient d'apprentissage est élevé, plus les pas entre deux mises à jour de la fonction coût seront importants. En modifiant ce paramètre, 
nous sommes confrontés à un compromis entre la vitesse d'entraînement et la convergence vers un solution satisfaisante.
L'implémentation basique de cet algorithme s'appelle le **batch gradient descent**. À chaque étape de calcul, il va calculer la dérivée partielle de toutes les observations ($m$). Cette méthode est donc longue pour les jeux de données très volumineux. 

### Descente du gradient : pour la régression linéaire

Dans le cas de la régression linéaire simple, la formule devient:

 $$
\left\{\begin{matrix}
\theta_0 =: \theta_0 - \alpha \frac{\partial}{\partial \theta_0} \frac{1}{m}\sum_{i=1}^m (h_{\theta}(x^{(i)}) - y^{(i)}) \\ 
\theta_1 =: \theta_1 - \alpha \frac{\partial}{\partial \theta_1} \frac{1}{m}\sum_{i=1}^m  (h_{\theta}(x^{(i)}) - y^{(i)})x^{(i)})
\end{matrix}\right.
 $$

En examinant cette formule, on voit bien que l'on fait déjà du **Machine Learning**, et plus précisément de l'**apprentissage supervisé**,
 car le modèle apprend bien à minimiser sa fonction d'erreur grâce aux données $x^{(i)}$ et $y^{(i)}$ de l'échantillon de référence.



""")

st.image("LR2.png")

st.markdown(r"""

Il existe une autre implémentation qui est le **stochastic gradient descent**, au lieu de prendre toutes les observations à chaque étape, 
l'algorithme va sélectionner au hasard une observation et calculer la dérivée partielle de celle-ci, 
en pratique cette méthode est assez efficace car elle impacte peu les performances et accélère énormément le temps d'entraînement.

Outre ces deux versions, il existe des alternatives modernes (et assez complexes) à la descente de gradient comme **L-BFGS, LMA**, etc.
""")

st.image("LR3.png")

st.markdown("""
La descente du gradient peut être sujette à la convergence dans des minimums locaux tandis que le problème d'optimisation posé pour la 
régression linéaire n'a qu'un seul minimum. **En d'autre mot la fonction coût de la régression linéaire est convexe**.
""")