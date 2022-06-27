## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OrpheeLetembe/P13_-METTEZ-A-L-ECHELLE-UNE-APPLICATION-DJANGO-EN-UTILISANT-UNE-ARCHITECTURE-MODULAIRE.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR-master`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR-master`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR-master`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR-master`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR-master`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`!
- `.quit` pour quitter

#### Panel d'administration


- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Prérequis

-  [Compte CircleCI](https://circleci.com/enterprise-trial-install/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--emea-en-brandLd-maxConv-lg-brand&utm_term=g_e-circleci_c__pipeline_20220513&utm_content=sem-google-dg--emea-en-brandLd-maxConv-lg-brand_keyword-text_eta-circleCI_exact-&gclid=Cj0KCQjwhqaVBhCxARIsAHK1tiMGaC9DxyEfRRxDyIrgRLNEvxQ5Qu_xt8Ar3unX56QvaqurB8xbwNUaAqQNEALw_wcB)
- [Compte Docker Hub](https://hub.docker.com/)
- [Compte Heroku](https://signup.heroku.com/)
- [Compte Sentry](https://sentry.io/signup/?gclid=CjwKCAjw77WVBhBuEiwAJ-YoJOtztPkl4oZIyfC_rbxd0b592BTCXiLpnfpb5Hu5gk_I9XnDeP1K7hoCT-UQAvD_BwE&gclid=CjwKCAjw77WVBhBuEiwAJ-YoJOtztPkl4oZIyfC_rbxd0b592BTCXiLpnfpb5Hu5gk_I9XnDeP1K7hoCT-UQAvD_BwE&utm_campaign=10530506129&utm_content=g&utm_medium=cpc&utm_source=google&utm_term=sentry)

### Fonctionnement

Le pipeline permet l'automatisation du processus de déploiement et se compose des phases suivantes :

- Les modifications apportées au code sont poussées vers le répertoire github du projet.
- circleci détecte le nouveau code et déclenche la phase de linting (flake8) et de tests (pytest).
- Une fois que le code a passé la phase précédente avec succès, une image du site pour Docker est construite et poussées vers le registre des conteneurs du Docker Hub.
- L'image est ensuite poussée vers le répertoire Heroku pour la mise en service.

### Etapes du déploiement

#### GitHub

- Créer un nouveau dépôt
- Aller sur cd/path/to/Python-OC-Lettings-FR-master
- Initialiser git `git init`
- Ajouter les fichiers `git add .`
- Ajouter un commit `git commit -m "commit`
- Pousser vers git 
  
  `git remote add origin https//github.com/nom utilisateur/nom projet.git`
  
    `git branch -M main`

  `git push -u origin main`

#### Docker 
- [Installer Docker Desktop](https://docs.docker.com/get-docker/)
- Connecter vous à Docker Hub pour créer un référentiel
- Cliquer sur Repositories puis Create Repository

[Documentation Docker](https://docs.docker.com/docker-hub/repos/)

#### Heroku

- Connecter vous à votre compte
- Ajouter une nouvelle application
- Ajouter sentry au Add-ons du projet (onglet Resources)
- Configurer le mode de déploiement (onglet Deploy)
  
    Deployment method : Github
- Choisir le projet à déployer
- Activer le déploiement automatique 
- Cocher la case `Wait for CI to pass before deploy`
- Configurer les variables d'environnement (onglet Settings)

  DJANGO_SETTINGS_MODULE : fichier setting de production
  
  SECRET_KEY : Générer [ici](https://djecrety.ir/)


#### Circleci

1- Connecter le projet

- Connecter vous à votre compte
- Cliquer sur l'onglet `Ajouter des projets` du tableau de bord
- Cliquer sur le nom du projet à connecter à circleci
- Cliquer sur `Start Building`
- Cliquer sur `Add Manually` (le projet contient déjà un fichier de configuration)

2- Configurer les variables d'environnement

- Cliquer sur `Project Settings` du tableau de bord
- Cliquer sur `Environment Variables`
- Configurer le variable d'environnement
  
  DOCKERHUB_LOGIN : nom d'utilisateur sur DOCKER

  DOCKERHUB_PASSWORD: mot de passe DOCKER 

  HEROKU_API_KEY: clé API de l'application Heroku (disponible à l'onglet Account settings)

  HEROKU_APP_NAME: nom de l'application Heroku
  
  HEROKU_LOGIN: nom d'utilisateur Heroku


