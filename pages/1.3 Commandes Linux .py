import streamlit as st


st.set_page_config(
    page_icon="🐧",
)

st.markdown("<h1 style='text-align: center; color: black;'>Les commandes Linux les plus utilisées</h1>", unsafe_allow_html=True)

st.markdown("""
### Win + A
Utiliser la combinaison `win + a` pour chercher une application.

### Ctrl + H 
Utiliser la combinaison `ctrl + h` pour voir les fichiers cachés.

click [ici](https://aciah-linux.org/spip.php?article226) pour plus de Combinaisons de touches.

### date
La commande `date` de Linux affiche et définit la date et l'heure du système.

la commande `date --utc` ou `date -u` affiche la date et heure du système en UTC (Temps universel coordonné).

Utilisez l'option `-date` pour afficher les dates passées ou dans le future de Linux. 
##### Exemples : 
- `date --date="2 year ago"`
- `date --date="yesterday"`
- `date --date="20 sec ago"`
- `date --date="next monday"`
- `date --date="5 day"`
- `date --date="tomorrow"`

### cal
La commande `cal` affiche un calendrier.

L'option `-A` pour afficher le nombre de mois après la date d'aujourd'hui
L'option `-B`   pour afficher le nombre de mois avant la date d'aujourd'hui

### echo $ PATH
`$ PATH` est une variable d'environnement liée à l'emplacement du fichier. Quand on tape une commande à exécuter, le système la recherche dans les répertoires spécifiés par `PATH` dans l'ordre spécifié.
 Vous pouvez afficher les répertoires spécifiés en tapant `echo $ PATH` dans le terminal. ... Vous pouvez rechercher votre chemin en tapant `echo $ PATH`.

 ### wich
 La commande `which` recherche l'exécutable dans les différents répertoires listés dans la variable d'environnement `PATH` 
 (et utilise le même algorithme que `BASH`).

 ##### Exemple : 
 La commande `which date` va chercher où se trouve la commande `date`

 ### man 
 La commande `man` permet de visionner le manuel d'une commande ou le manuel d'un fichier de configuration.
 ##### Exemple : 
 `man date`

 ### history
 la commande `history` permet de remonter dans les commandes que nous avons passées. Après cette commande, on peut taper `! 80` par exemple pour exécuter la commande numéro 80 dans l'hestorique.

### ls
La commande `ls` répertorie les fichiers et les répertoires dans le système de fichiers et affiche des informations détaillées sur eux. 

##### Exembles :
- `ls -l` : pour afficher le format de liste longue.
- ls -l -a = ls -la = ls -al = ls -ll : pour afficher le format de liste longue avec les fichier cachés.

### cd
La commande `cd` vous permet de changer de répertoire (`cd` = change directory). 
Quand vous ouvrez un terminal en mode utilisateur vous êtes dans votre répertoire personnel (/home/utilisateur). 

Pour "remonter" d'un répertoire (aller à son parent) on utilise la commande `cd ..`

### pwd
Son nom signifie en anglais « print working directory ». Elle permet d'afficher le chemin d'accès vers le répertoire où se situe l'utilisateur qui a entré la commande.

### xdg-open
 La commande `xdg-open` dans le système Linux est utilisée pour ouvrir un fichier ou une URL dans l'application préférée de l'utilisateur.
 Exemple : `xdg-open /Download`

 ### mkdir 
 C'est pour créer un dossier

 ### touch
 C'est pour créer des fichiers vides


 ### rm
 La commande `rm` est utilisée pour supprimer des fichiers et des répertoires sous Linux en ligne de commandes. 
 - `rm FICHIER` pour supprimer un fichier
 - `rm /tmp/exemple.txt` pour supprimer le fichier /tmp/exemple.txt depuis n'importe quel emplacement .
 - `rm -r` pour supprimer un répertoires vide
 - `rm -d` pour supprimer un répertoires non vide


 ### cp
 `cp` signifie copie. Cette commande est utilisée pour copier des fichiers ou un groupe de fichiers ou de répertoires. 

 ### mv
 La commande `mv` (pour move) permet de déplacer un fichier, répertoire ou tout arborescence sur Linux. 

 ### touch
 La commande `touch` de Linux est principalement utilisée pour créer des fichiers vides
- `touch file{1..100}.txt` cette commande va créer les fichiers : file1.txt, file2.txt, ... file100.txt

### cat
la commande `cat nomdufichier.txt` va visualiser le contenu d'un fichier

### less
Affiche le contenu d'un fichier ou d'une sortie de commande, une page à la fois. 

### head & tail
- `head` pour afficher le début d'un fichier (texte).
- `tail` pour imprimer les derniers numéros ou la queue d'une entrée. 

### nano
Pour éditer un texte (`ctrl+x` pour sortir)


## Exemple : 
la commande : `mkdir -p A/B/C/D/E` va créer un dossier A et sous-dossier B dans A et sous-dossier C dans B ....
la commande : `touch {A, A/B, A/B/C, A/B/C/D, A/B/C/D/E}/test.txt` va créer un fichier text.txt dans A et dans le sou-dossier B et dans le sous-sous-dossier C et ....
""")