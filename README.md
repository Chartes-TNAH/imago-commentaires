# imago-commentaires : Présentation de corpus d'images

Dans le cadre d'un projet de recherche, il est souvent possible de vouloir simplement mettre en ligne un ensemble de commentaires d'images. Dans ce cadre, vous construirez une application qui correspond aux points suivants
- Les images seront issues de manifestes IIIF tels que https://data.getty.edu/museum/api/iiif/7792/manifest.json (cf. Lien vers IIIF sur une page du Getty et Page originale
- On s'intéressera à l'usage de IIIF Prezi et de ressources issues de https://github.com/IIIF/awesome-iiif
- Une base de données utilisateur sera mise en place pour pouvoir ajouter des commentaires.
- Les commentaires porteront sur : une image (via son manifeste) avec un texte et un auteur. Le texte supportera la mise en page markdown ou du html (cf. Snippet pour utilisation de markdown avec flask
- Des commentaires de tests (type Lorem Ipsum) seront fournis pour pouvoir faire fonctionner l'outil
- Les métadonnées de l'image seront affichées à partir du manifeste.
