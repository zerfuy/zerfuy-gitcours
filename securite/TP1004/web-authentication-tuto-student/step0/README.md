# Presentation de la structure du code Flask
## 1 Objectif
Le code présentant dans les différentes étapes sont les codes d'un serveur web Flask permettant de répondre à des requètes http et d'enregistrer des utilisateurs dans une base de données
## 2 Structure de fichiers
L'application présente la structure de fichiers suivante:
 ```
-web_server
    |-model
        |-db.py
        |-UserRestCrt.py
    |-route
        |-authCustom.py
        |-authStd.py
    |-static
        |-js
        |-lib
        |-my_css.css
    |-templates
        |-auth
            |-failureAuth.html
            |-login.html
            |-register.html
            |-successAuth.html
    |-tools
        |-CipherTools.py
    |-app.py
    |-schema.sql
 ```
 - Le fichier ```app.py``` est le fichier principale qui va lancer le serveur web Flask
 - Le fichier ```schema.sql``` va être appelé par ```db.py``` pour initaliser la base de données (```sqlite```) locale
 - le répertoire ```/model``` contient le outil d'interaction avec la base de données:
   - ```db.py``` permet d'interagir avec la base de données
   - ```UserRestCrt.py``` permet d'ajouter un utilisateur à la base de données (end point ```/user/add```)
- Le répertoire ```/route``` contient les fichiers permettant de gérer les end points d'authentification du serveur web.
- Le répertoire ```/static``` contient tout le contenu static du serveur web accessible depuis un web browser.
- Le répertoire ```/template``` contient les vues utilisables par Flask (création/redirection)
-  Le répertoire ```/tools``` contient les utilitaires utilisés pour la gestion d'authentification (digest de contenus, création de token, vérification de token, etc...)

## 3 Récupération des dépendances 

### 3.1  Création d'un virtual env
- A la racine du repo créé créer un virtual env qui fonctionnera avec une version de python >3.5
```
$ python -m  venv venv
```
- Activer le virtualenv
```
$ source venv/bin/activate
(venv) $
```
- Une fois le virtualenv activé les dépendances installées se feront uniquement dans cet environnement

Pour désactiver le virtualenv entrer simplement la commande ```deactivate```

### 3.2  Installation des dépendances
- installer les dépendances présentes dans le fichier ```requirements.txt```

```
pip install -r ../requirements.txt
```

## 4 Démarrage du server Flask
- Définissez les variables suivantes d'env.
```
$ cd ../step1
$ cd web_server
$ export FLASK_APP=app.py
```

Pour windows utiliser cette commande  ```$ set FLASK_APP=app.py ```

- Créer la base de données associée au server web
```
$ flask init-db
```
- Démarrer le server web
```
$ flask run
```
