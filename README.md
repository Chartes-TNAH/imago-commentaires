# Imaginatiiif

## Définition :

Imaginatiiif est une application permettant d'associer un objet issu d'un manifeste IIIF avec un commentaire rédigé par l'utilisateur.

## Comment utiliser Imaginatiiif :

Imaginatiiif nécessite la création d'un compte pour chaque utilisateur, permettant ainsi la création d'un corpus personnel. Une fois l'utilisateur enregistré, la page de création de commentaire demande uniquement le lien IIIF de l'oeuvre concernée et le commentaire qu'on lui associe. Imaginatiiif se charge ensuite de récupérer, grâce au lien IIIF, les images et les métadonnées liées à l'oeuvre.
La page ainsi obtenue affiche donc les images de l'oeuvre, ses métadonnées et le commentaire de l'utilisateur. Il est ensuite possible à l'utilisateur de modifier ou supprimer son commentaire.

## Comment fonctionne Imaginatiiif :

Les différentes pages s'appuient sur les langages HTML, CSS, JavaScript et Python 3, ainsi que sur une base de données MySQL.

## Comment installer Imaginatiiif :

* Télécharger le dossier GitHub.
* Nous recommandons la création d'un environnement virtuel d'après le fichier requirements.txt .
* Ouvrir le premier dossier "imaginatiiif" et lancer le fichier run.py .

### A savoir :

Cette application a été créée comme exercice dans le cadre de la validation du cours de Python du master TNAH de l'Ecole nationale des chartes (Paris).
Les consignes en étaient les suivantes :

Dans le cadre d'un projet de recherche, il est souvent possible de vouloir simplement mettre en ligne un ensemble de commentaires d'images. Dans ce cadre, vous construirez une application qui correspond aux points suivants
- Les images seront issues de manifestes IIIF tels que https://data.getty.edu/museum/api/iiif/7792/manifest.json (cf. Lien vers IIIF sur une page du Getty et Page originale
- On s'intéressera à l'usage de IIIF Prezi et de ressources issues de https://github.com/IIIF/awesome-iiif
- Une base de données utilisateur sera mise en place pour pouvoir ajouter des commentaires.
- Les commentaires porteront sur : une image (via son manifeste) avec un texte et un auteur. Le texte supportera la mise en page markdown ou du html (cf. Snippet pour utilisation de markdown avec flask
- Des commentaires de tests (type Lorem Ipsum) seront fournis pour pouvoir faire fonctionner l'outil
- Les métadonnées de l'image seront affichées à partir du manifeste.
