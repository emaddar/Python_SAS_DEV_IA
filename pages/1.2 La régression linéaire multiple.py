import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# plt.rcParams.update(plt.rcParamsDefault)
# from scipy import stats
# import numpy as np

st.set_page_config(
    page_icon="🐍",
)
# st.markdown("<h1 style='text-align: center; color: black;'>La régression linéaire</h1>", unsafe_allow_html=True)

st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--Xt-qnrk0--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/a2wdgocn3n7wbk7g23eb.jpg")

st.markdown(r"""
# La régression linéaire multiple 
C'est une régression linéaire à plusieurs variables explicatives $X1$, $X2$, ...

### Forme de la fonction $h(x)$
$$
h_{\theta}(X) = \theta_0 + \theta_1 X1 + \theta_2 X2 + \theta_3 X3 + ... + \theta_n Xn
$$
en forme matricielle :
$$
h_{\theta}(X) = \begin{bmatrix}
\theta_0 &\theta_1  &\theta_2  &...  &\theta_n 
\end{bmatrix}\begin{bmatrix}
X_0\\ 
X_1\\ 
X_2\\ 
\vdots\\ 
X_n
\end{bmatrix} = \theta^T X
$$
avec $X_0 = 1$

### La fonction coût $J$ :
$$
J(\theta) = \frac{1}{2m}\sum_{i=1}^m (h_{\theta}(x^{(i)}) - y^{(i)})^2 = \frac{1}{2m} (X\theta - y)^T(X\theta - y) 
$$

### Forme de la descente du gradient :
répéter jusqu'à convergence \{
$$
\theta_j =: \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta) \\
\texttt{                   }=: \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m (h_{\theta}(x^{(i)}) - y^{(i)})x_j^{(i)}
$$
mettre à jour simultanément $\theta_j$ avec $j = 0,1,2,...n$

\}

#### Vectorisation
répéter jusqu'à convergence  \{
$$
\theta =: \theta - \alpha \frac{1}{m} \sum_{i=1}^m (h_{\theta}(x^{(i)}) - y^{(i)})x^{(i)}
$$
\}
""")
