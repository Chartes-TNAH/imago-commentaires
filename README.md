# imago-commentaires : Présentation de corpus d'images

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

L'application prend en charge les images au format IIIF. Elle affiche l'ensemble des images déclarées dans le manifest (une ou plusieurs vues selon la structure de l'objet numérisé) et l'ensemble des métadonnées lorsque celles-ci sont déclarées  au premier niveau du fichier JSON-LD. Ainsi nous avons testé l'ajout d'images et de commentaires pour des manifests provenant de quatre établissements différents : Le Getty, la BnF, La bodleian library et Harvard museum.

L'application comprend deux tables SQL : une pour gérer les comptes utilisateurs et une pour gérer les commentaires.
Le fichier datamodel permet de générer les tables ainsi qu'un utilisateur et deux commentaires. Ces commentaires comprennent des liens vers des images au format IIIF issues de manifests de la BnF et du Getty.

Deux autres  liens vers des manifests d'images en IIIF sont proposés dans l'issue #24 :
Un de la Bodelian Library et un autre de Harvard museum.

