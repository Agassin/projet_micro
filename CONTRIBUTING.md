# Guide de Contribution - Web App

Merci de votre intérêt pour contribuer à ce projet ! 🎉 Ce guide vous aidera à comprendre comment contribuer efficacement.

## 📋 Table des matières

- [Introduction](#introduction)
- [Types de contributions](#types-de-contributions)
- [Comment commencer](#comment-commencer)
- [Processus de contribution](#processus-de-contribution)
- [Standards et conventions](#standards-et-conventions)
- [Processus de review](#processus-de-review)
- [Communication](#communication)
- [Reconnaissance](#reconnaissance)
- [Ressources utiles](#ressources-utiles)

## 🎯 Introduction

Ce projet vise à créer une application web Django moderne et accessible. Nous accueillons chaleureusement les contributions sous forme de code, documentation, tests, rapports de bugs ou suggestions d'améliorations.

### Vision du projet
Développer une application web robuste, maintenable et bien documentée qui serve de référence pour les bonnes pratiques Django.

## 🤝 Types de contributions

### Code
- **Nouvelles fonctionnalités** : Ajout de fonctionnalités demandées
- **Corrections de bugs** : Résolution de problèmes identifiés
- **Refactorisation** : Amélioration de la qualité du code existant

### Documentation
- Amélioration des guides existants
- Ajout d'exemples d'utilisation
- Traductions et clarifications
- Mise à jour du README et de la documentation technique

### Tests
- Ajout de tests unitaires
- Tests d'intégration
- Amélioration de la couverture de tests

### Rapports de bugs
- Description précise du problème
- Étapes pour reproduire le bug
- Comportement attendu vs réel
- Information de l'environnement

### Suggestions
- Propositions d'améliorations
- Feedback sur l'ergonomie
- Idées d'optimisation

## 🚀 Comment commencer

### Prérequis techniques
- Python 3.8+
- Git
- Django 3.2+
- Un navigateur moderne

### Configuration de l'environnement de développement

#### 1. Cloner le repository
```bash
git clone <repository-url>
cd projet_micro/web_app
```

#### 2. Créer un environnement virtuel
```bash
# Sur Windows
python -m venv venv

# Sur Mac/Linux
python -m venv venv
```

#### 3. Activer l'environnement virtuel
```bash
# Sur Windows
venv\Scripts\activate

# Sur Mac/Linux
source venv/bin/activate
```

#### 4. Installer les dépendances
```bash
# Installer les dépendances de base
pip install django

# OU installer toutes les dépendances de développement (recommandé)
pip install -r requirements-dev.txt
```

#### 5. Initialiser la base de données
```bash
python manage.py migrate
```

#### 6. Créer un utilisateur administrateur (optionnel)
```bash
python manage.py createsuperuser
```

#### 7. Démarrer le serveur de développement
```bash
python manage.py runserver
```

Le serveur sera disponible à `http://127.0.0.1:8000/`

## 📝 Processus de contribution

### Avant de commencer
1. Vérifiez que l'issue n'a pas déjà été traitée
2. Créez une nouvelle issue si nécessaire pour discuter de votre contribution
3. Attendez une réponse avant de commencer un travail important

### Vérifier le CI/CD
- Poussez vos changements sur `master` ou ouvrez une PR.
- Ouvrez l'onglet **Actions** sur GitHub.
- Le workflow doit s'exécuter et afficher un statut **succeed**.
- En cas d'échec, ouvrez le job et lisez le log de l'étape en erreur.

### Workflow Git recommandé

#### 1. Cloner le repository
Pour cloner le repository, utilisez la commande suivante :

```bash
git clone https://github.com/Agassin/projet_micro.git
cd projet_micro/web_app
```

#### 2. Créer une branche

```bash
# patern de nommage : trigramme/feat|bugfix|hotfix|docs|test/description-breve-de-la-branche
git checkout -b ase/feat/description-breve-de-la-feature
```

**Convention de nommage des branches :**
- `trigramme/feat/description-breve` - pour les nouvelles fonctionnalités
- `trigramme/bugfix/description-du-bug` - pour les corrections de bugs
- `trigramme/hotfix/description-critique` - pour les corrections critiques
- `trigramme/docs/description-docs` - pour les mises à jour de documentation
- `trigramme/test/description-test` - pour l'ajout de tests

#### 3. Effectuer vos modifications
1. Suivez les standards de code du projet (voir ci-dessous)
2. Testez vos modifications localement
3. Assurez-vous que le serveur démarre correctement

#### 4. Committer vos modifications
```bash
git commit -m "type: description concise"
```

**Format des messages de commit :**
- `feat(#<issue-number>): ajouter une nouvelle fonctionnalité`
- `fix(#<issue-number>): corriger un bug`
- `docs(#<issue-number>): mettre à jour la documentation`
- `test(#<issue-number>): ajouter des tests`
- `refactor(#<issue-number>): améliorer le code existant`
- `style(#<issue-number>): changements de formatage`

Exemple complet :
```
feat(#123): ajouter la page de profil utilisateur

- Création de la vue ProfileView
- Ajout du template profile.html
- Mise à jour des URLs
- Ajout des tests unitaires correspondants
```

#### 5. Avant de soumettre une Pull Request
1. Mettez à jour votre branche avec la branche principale
```bash
git pull origin main
```

2. Testez complètement vos modifications
3. Vérifiez que la base de données fonctionne correctement
4. Assurez-vous que tous les fichiers statiques sont chargés correctement

#### 6. Soumettre une Pull Request
1. Poussez votre branche
```bash
git push origin trigramme/feat/description-breve-de-la-branche
```

2. Ouvrez une Pull Request sur GitHub
3. Remplissez le template de Pull Request fourni
4. Décrivez clairement :
   - Le problème que vous résolvez
   - Comment vous l'avez résolu
   - Les tests effectués
   - Les captures d'écran si pertinent

## 📐 Standards et conventions

### Style de code - PEP 8

Suivez les conventions Python PEP 8 (https://peps.python.org/pep-0008/):
- Utilisez 4 espaces pour l'indentation
- Longueur max des lignes : 100 caractères (au lieu de 79 pour plus de flexibilité)
- Utilisez des noms explicites pour les variables et les fonctions
- Respectez les 2 lignes blanches entre les définitions de fonctions au niveau du module

#### Configuration de Flake8

Un linter Flake8 a été mis en place pour garantir le respect automatique de PEP 8.

**Installation du linter :**
```bash
# Option 1 : Installer uniquement Flake8
pip install flake8

# Option 2 : Installer toutes les dépendances de développement (recommandé)
pip install -r requirements-dev.txt
```

**Utilisation du linter :**
```bash
# Vérifier l'ensemble du projet
python -m flake8 web_app/

# Vérifier un fichier spécifique
python -m flake8 web_app/core/models.py

# Afficher les statistiques détaillées
python -m flake8 web_app/ --statistics

# Afficher le code source des erreurs
python -m flake8 web_app/ --show-source
```

**Configuration du linter :**
Le fichier `.flake8` à la racine du projet contient la configuration :
- **max-line-length** : 100 caractères (règle E501)
- **Répertoires exclus** : migrations, venv, __pycache__, staticfiles, etc.
- **Affichage** : Source code et statistiques activés

**Types d'erreurs courantes détectées :**
- **E302** : 2 lignes blanches attendues avant une définition
- **E501** : Ligne trop longue (> 100 caractères)
- **F401** : Import inutilisé
- **W503** : Saut de ligne avant un opérateur binaire (ignoré)

**Avant de soumettre une Pull Request :**
```bash
# Vérifiez qu'il n'y a pas d'erreurs Flake8
python -m flake8 web_app/

# Le linter ne doit retourner aucune erreur
```

Exemple :
```python
# ✅ Bon
def calculate_user_age(birth_year):
    current_year = 2024
    return current_year - birth_year

# ❌ Mauvais
def calc_age(by):
    return 2024 - by
```

### Documentation des fonctions

Documentez toutes vos fonctions avec des docstrings :
```python
def get_user_profile(user_id):
    """
    Récupère le profil d'un utilisateur.
    
    Args:
        user_id (int): L'identifiant unique de l'utilisateur
    
    Returns:
        Profile: L'objet profil de l'utilisateur
        
    Raises:
        Profile.DoesNotExist: Si le profil n'existe pas
    """
    return Profile.objects.get(user_id=user_id)
```

### Tests obligatoires

Tout code nouveau doit être accompagné de tests :
- Tests unitaires pour les fonctions utilitaires
- Tests d'intégration pour les vues
- Couverture minimale : 80%

```python
from django.test import TestCase
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name="Test User")
    
    def test_profile_creation(self):
        self.assertEqual(self.profile.name, "Test User")
```

### Structure du Projet

Respectez la structure existante :
- `core/` - Application Django principale
  - `models.py` - Modèles de données
  - `views.py` - Vues
  - `tests.py` - Tests unitaires
  - `static/` - Fichiers CSS et JavaScript
    - `css/` - Feuilles de style
    - `js/` - Scripts JavaScript
  - `templates/` - Templates HTML
- `static_site/` - Configuration Django
- `_ext_src/` - Ressources externes

### Points importants

- ✅ Suivre PEP 8 pour tout code Python
- ✅ Tests unitaires obligatoires pour les nouvelles fonctionnalités
- ✅ Commenter le code complexe
- ✅ Pas de breaking changes sans discussion préalable
- ✅ Mettez à jour la documentation si nécessaire

## 🔍 Processus de review

### Qui peut reviewer
- Les mainteneurs du projet
- Les contributeurs expérimentés
- Tout membre de la communauté peut donner du feedback

### Critères d'acceptation
- ✅ Code respecte les standards du projet
- ✅ Tests existants passent
- ✅ Nouveaux tests couvrent le code ajouté
- ✅ Pas de dépendances non nécessaires
- ✅ Documentation mise à jour

### Temps de réponse attendu
- Revue initiale : 1-2 jours
- Feedback sur les changements demandés : 1 jours
- Approbation finale : 3 jours

### Processus d'approbation
1. Au moins une approbation d'un mainteneur
2. Tous les commentaires adressés
3. Tous les tests passent
4. Merge par un mainteneur

## 💬 Communication

### Canaux de discussion
- **Issues GitHub** : Pour les bugs et les demandes de fonctionnalités
- **Pull Requests** : Pour les discussions sur le code
- **Email** : Pour les questions sensibles

### Comment poser des questions
- Vérifiez d'abord les issues existantes et la documentation
- Posez votre question de manière claire et concise
- Fournissez du contexte et des exemples
- Restez respectueux et constructif

### Étiquette de communication
- Soyez respectueux et inclusif
- Acceptez les critiques constructives
- Aidez les autres contributeurs quand vous pouvez
- Évitez le spam ou les messages hors-sujet
- Les commentaires irrespectueux seront supprimés

## 🌟 Reconnaissance

### Comment les contributeurs sont crédités
- Tous les contributeurs sont listés dans le fichier CONTRIBUTORS.md
- Les merges majeurs sont annoncés dans les release notes
- Crédits dans le README pour les contributions significatives

## 📚 Ressources utiles

### Documentation technique
- [Django Documentation](https://docs.djangoproject.com/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Documentation](https://git-scm.com/doc)

### Tutoriels recommandés
- Django for Beginners (https://www.youtube.com/watch?v=sm1mokevMWk)
- Real Python Django Tutorials (https://realpython.com/tutorials/django/)
- Official Django Tutorial (https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

### Outils recommandés
- `flake8` - Linter Python pour PEP 8 (configuré dans `.flake8`)
- `black` - Formateur de code Python
- `isort` - Tri automatique des imports
- `pytest` - Framework de test
- `Django Debug Toolbar` - Outil de debugging Django

### Installation des outils de développement
```bash
pip install -r requirements-dev.txt
```

Cela installera :
- `flake8` - Linter PEP 8
- `black` - Formateur de code
- `isort` - Outil de tri des imports
- `pytest` & `pytest-django` - Framework de test
- `Django Debug Toolbar` - Outil de debugging

## ❓ FAQ

**Q : Dois-je demander la permission avant de travailler sur une fonctionnalité ?**
A : Pour les petites corrections, non. Pour les grandes fonctionnalités, ouvrez une issue d'abord pour discuter.

**Q : Combien de temps avant que ma PR soit mergée ?**
A : Cela dépend de la complexité. Généralement 3-4 jours pour les petites PR, plus long pour les grandes.

**Q : Je suis novice en développement, puis-je quand même contribuer ?**
A : Absolument ! Nous encourageons les contributions de tous les niveaux. Cherchez les issues avec un label "good first issue".

**Q : Qu'est-ce qu'un breaking change ?**
A : Une modification qui casse la compatibilité avec le code existant. Exemple : changer la signature d'une fonction publique.

**Q : Comment signaler un bug ?**
A : Ouvrez une issue avec le label "bug", décrivez le problème, les étapes pour le reproduire, et votre environnement.

---

**Merci pour votre contribution ! Nous apprécions votre aide pour améliorer ce projet. 🙏**

## Questions ou Besoin d'Aide ?

Contactez les mainteneurs du projet via le serveur Discord https://discord.gg/Zc7dDQyPSQ.

## Licence

En contribuant à ce projet, vous acceptez que vos contributions soient sous la même licence que le projet.
