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

L'application Imago-commentaires offre la possibilité de constituer un corpus d'images au format IIIF et de commenter chacune des images du coprus.

L'utilisateur doit au préalable créer un compte sur le site qui lui donne accès à des fonctionnalités propres :
- l'ajout d'images et de commentaires (L'utilisateur (compte actif) est automatiquement authentifié comme auteur du commentaire).
- la modification de commentaires (la date de la modification figure dans le commentaire).
- la suppression de commentaires.

Il est possible de voir les commentaires des autres uitilisateurs sans pouvoir intervenir dessus.

L'application prend en charge les images au format IIIF. Elle affiche l'ensemble des images déclarées dans le manifeste (une ou plusieurs vues selon la structure de l'objet numérisé) et l'ensemble des métadonnées lorsque celles-ci sont déclarées  au premier niveau du fichier JSON-LD. Ainsi nous avons testé l'ajout d'images et de commentaires pour des manifestes provenant de quatre établissements différents : Le Getty, la BnF, la bodleian library et Harvard art museum.

L'application comprend deux tables SQL : une pour gérer les comptes utilisateurs et une pour gérer les commentaires.
Le fichier datamodel permet de générer les tables ainsi qu'un utilisateur et deux commentaires. Ces commentaires comprennent des liens vers des images au format IIIF issues de manifests de la BnF et du Getty.

Deux autres  liens vers des manifestes d'images en IIIF sont proposés dans l'issue #37 :

- Exemple de manifeste de la digital Bodleian library :
Shelfmark: MS. Canon. Ital. 143, map folio 3
title: [Close-up of Venice and Genoa in portolan chart of the central and western Mediterranean and part of the Atlantic]
Date: 1559
Manifeste Json : https://iiif.bodleian.ox.ac.uk/iiif/manifest/c233ee09-bedc-4f21-89ba-09449b1ba69b.json

- Exemple de manifeste d'Harvard Art Museums (manifest JSON-LD) :
Libellé: The Apostle Jean Journet
Date: 1850
Object Number: M26222
Manifeste en Json: https://iiif.harvardartmuseums.org/manifests/object/55407 (ouvrir dans un éditeur de texte)
Manifeste interprété avec le visualiseur Mirador : https://iiif.harvardartmuseums.org/viewers/mirador?manifest=https://iiif.harvardartmuseums.org/manifests/object/55407

Nous n'avons pas réussi à afficher les images du manifeste de Harvard art museum directement dans l'application, mais un lien est proposé à la place des images et elles s'affichent dans une nouvelle fenêtre.




