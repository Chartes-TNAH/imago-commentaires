from imaginatiiif.app import db, config_app, login
from imaginatiiif.modeles.utilisateurs import User
from imaginatiiif.modeles.donnees import Comment
from unittest import TestCase


class Base(TestCase):
    comments = [
        Comment(
            comment_nom='Photo Bradley & Rulofson',
            comment_commentaire='Essaie1',
            comment_lien='http://gallica.bnf.fr/iiif/ark:/12148/btv1b8453687c/manifest.json'

        ),
        Comment(
            comment_nom='Pont du Carrousel',
            comment_commentaire='Essaie2',
            comment_lien='https://data.getty.edu/museum/api/iiif/61899/manifest.json'

        ),

    ]

    def setUp(self):
        self.app = config_app("test")
        self.db = db
        self.client = self.app.test_client()
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.drop_all(app=self.app)

    def insert_all(self, comments=True):
        # On donne à notre DB le contexte d'exécution
        with self.app.app_context():
            if comments:
                for fixture in self.comments:
                    self.db.session.add(fixture)
            self.db.session.commit()