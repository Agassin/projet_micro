# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement
# Sur Windows:
venv\Scripts\activate
# Sur Mac/Linux:
source venv/bin/activate

# Installer Django
pip install django

# Créer le projet Django
django-admin startproject static_site .

# Créer l'application core
python manage.py startapp core

# Étape 10: Instructions pour exécuter le projet
# Initialiser la base de données :

python manage.py migrate

# Créer un superutilisateur (optionnel) :

python manage.py createsuperuser

# Démarrer le serveur de développement :

python manage.py runserver

# modif pour création de pull request