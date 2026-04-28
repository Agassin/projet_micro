# Guide de Contribution - Web App

## Configuration de l'Environnement de Développement

### 1. Cloner le repository
```bash
git clone <repository-url>
cd projet_micro/web_app
```

### 2. Créer un environnement virtuel
```bash
# Sur Windows
python -m venv venv

# Sur Mac/Linux
python -m venv venv
```

### 3. Activer l'environnement virtuel
```bash
# Sur Windows
venv\Scripts\activate

# Sur Mac/Linux
source venv/bin/activate
```

### 4. Installer les dépendances
```bash
pip install django
```

### 5. Initialiser la base de données
```bash
python manage.py migrate
```

### 6. Créer un utilisateur administrateur (optionnel)
```bash
python manage.py createsuperuser
```

### 7. Démarrer le serveur de développement
```bash
python manage.py runserver
```

Le serveur sera disponible à `http://127.0.0.1:8000/`

## Processus de Contribution

### Avant de commencer
1. Vérifiez que l'issue n'a pas déjà été traitée
2. Créez une nouvelle branche pour votre fonctionnalité
```bash
git checkout -b feature/nom-de-la-feature
```

### Pendant la contribution
1. Suivez les conventions de code du projet
2. Testez vos modifications localement
3. Assurez-vous que le serveur démarre correctement

### Avant de soumettre une Pull Request
1. Mettez à jour votre branche avec la branche principale
```bash
git pull origin main
```

2. Testez complètement vos modifications
3. Vérifiez que la base de données fonctionne correctement
4. Assurez-vous que tous les fichiers statiques sont chargés correctement

### Soumettre une Pull Request
1. Poussez votre branche
```bash
git push origin feature/nom-de-la-feature
```

2. Ouvrez une Pull Request sur GitHub
3. Décrivez clairement les modifications apportées
4. Attendez la revue et les commentaires

## Structure du Projet

- `core/` - Application Django principale
  - `models.py` - Modèles de données
  - `views.py` - Vues
  - `static/` - Fichiers CSS et JavaScript
  - `templates/` - Templates HTML
- `static_site/` - Configuration Django
- `_ext_src/` - Ressources externes

## Directives de Code

- Utilisez des noms explicites pour les variables et les fonctions
- Commentez le code complexe
- Testez vos modifications avant de soumettre
- Suivez la structure existante du projet

## Questions ou Besoin d'Aide ?

Ouvrez une issue ou contactez les mainteneurs du projet.

## Licence

En contribuant à ce projet, vous acceptez que vos contributions soient sous la même licence que le projet.
