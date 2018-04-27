from flask import render_template, request, flash, redirect

from .app import app, login
from .modeles.donnees import Comment
from .modeles.utilisateurs import User
from .constantes import COMMENTAIRE_PAR_PAGE
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def accueil():
    """ Route permettant l'affichage d'une page accueil avec 5 derniers commentaires enregistrés
    :return: page html d'accueil
    """

    commentaires = Comment.query.order_by(Comment.comment_id.desc()).limit(5).all()
    return render_template("pages/accueil.html", nom="Imaginatiiif", commentaires=commentaires)

@app.route("/comments")
def all_comments():
    """ Route permettant l'affichage d'une page avec touts commentaires ajoutés
    :return: page html avec une liste de commentaires
    """
    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    commentaires = Comment.query.order_by(Comment.comment_id).paginate(page=page, per_page=COMMENTAIRE_PAR_PAGE)
    return render_template("pages/all_comments.html", nom="Imaginatiiif", commentaires=commentaires, page=page)

@app.route("/comment/<int:comment_id>")

def commentaire(comment_id):
    """ Route permettant l'affichage d'une page avec le commentaire, l'image et les métadonnées à partir d'un manifeste
       :param comment_id: Identifiant numérique du commentaire
       :return: page html d'un commentaire
       """
    import requests

    unique_commentaire = Comment.query.get(comment_id)
    utilisateur = User.query.get(unique_commentaire.comment_user_id)
    r = requests.get(unique_commentaire.comment_lien)
    data = r.json()
    simplified = []
    image = []

    if data["attribution"] == "Harvard Art Museums":
        url_image = data["rendering"]["@id"]
        image.append(url_image)

    else:
        for item in data["sequences"][0]["canvases"]:
            try:
                url_image = item["images"][0]["resource"]["@id"]
                image.append(url_image)

            except:
                error = "Pas pu récupérer d'image"
                data = {}

    for item in data["metadata"]:
        try:
            identifier = item["label"]

            if ["attribution"] == "Bibliothèque nationale de France":
                if identifier == "Language":
                    simplified.append(item["value"][1]["@value"])

                elif identifier == "Format":
                    simplified.append(item["value"][0]["@value"], item["value"][1]["@value"],
                                      item["value"][2]["@value"])

                elif identifier == "Type":
                    simplified.append(item["value"][1]["@value"], item["value"][3]["@value"])

                else:
                    simplified.append(identifier)

        except:
            error = 'Pas pu récupérer les données'
            data = {}

    return render_template('pages/comment.html', nom='Imaginatiiif',
                           commentaire=unique_commentaire,
                           user=utilisateur,
                           data=data.get('metadata'),
                           img=image)


@app.route("/modif_commentaire/<int:comment_id>", methods=["GET", "POST"])
@login_required
def modif_commentaire(comment_id):
    """ Route permettant modifier le commentaire
        :param comment_id: Identifiant numérique du commentaire
        :return: page html avec un formulaire pour modifier le commentaire"""
    commentaire = Comment.query.get(comment_id)
    if current_user.get_id() != commentaire.comment_user_id:
        flash("Vous n'avez pas l'autorisation de modifier ce commentaire", 'error')
        return render_template("pages/modif_commentaire.html", commentaire=commentaire)

    status, donnees = Comment.modif_commentaire(
        id=comment_id,
        nom=request.form.get("nom", None),
        lien=request.form.get("lien", None),
        commentaire=request.form.get("commentaire", None),
    )

    if status is True:
        flash('Merci de votre contribution', 'success')
        return redirect('/')

    else:
        flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
        unique_commentaire = Comment.query.get(comment_id)
        return render_template("pages/modif_commentaire.html", commentaire=unique_commentaire)


@app.route("/suppression/<int:comment_id>", methods=["GET", "POST"])
@login_required
def suppression_comment(comment_id):
    """ Route pour supprimer le commentaire
    :param comment_id : identifiant numérique du commentaire
    :return: page html de suppression
    """

    unique_commentaire = Comment.query.get(comment_id)
    '''if current_user.get_id() != unique_commentaire.comment_user_id:
        flash("Vous n'avez pas l'autorisation de supprimer ce commentaire", 'error')
        return render_template("pages/comment.html", commentaire=commentaire)'''
    if request.method == "GET":
        return render_template("pages/suppression_comment.html", unique=unique_commentaire, all_comments=all_comments)
    else:
        status = Comment.delete_comment(comment_id=comment_id)
        if status is True :
            flash("Votre commentaire a été supprimé !", "success")
            return redirect("/")
        else:
            flash("La suppression a échoué.", "danger")
            return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def inscription():
    """ Route gérant les inscriptions
    :return: page html d'inscription
    """

    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")


@app.route("/nomcommentaire", methods=["GET", "POST"])
@login_required
def nomcommentaire():
    """ Route gérant les ajouts des commentaires
    :return: page html d'ajout de commentaire
    """

    if request.method == "POST":
        statut, donnees = Comment.creercomment(
            nom=request.form.get("nom", None),
            commentaire=request.form.get("commentaire", None),
            lien=request.form.get("lien", None),
            user_id=current_user.get_id()

        )
        if statut is True:
            flash("Enregistrement effectué", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/nomcommentaire.html")
    else:
        return render_template("pages/nomcommentaire.html")


@app.route("/utilisateur")
def comment_auteur():
    """ Route permettant l'affichage d'une page avec les commentaires d'un auteur
    :return: page html avec les commentaires d'un auteur autorisé
        """

    commentaires = Comment.query.filter(Comment.comment_user_id == current_user.get_id()).all()
    return render_template("pages/comment_auteur.html", nom="Imaginatiiif", commentaires=commentaires)


@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    :return: page html de connection
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")

    return render_template("pages/connexion.html")


login.login_view = 'connexion'


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    """ Route gérant les déconnexions
        :return: page html d'acceuil
        """
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect("/")
