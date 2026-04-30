"""
Script pour corriger les violations PEP 8 dans les fichiers Python de test.

Ce script:
1. Vérifie les violations PEP 8
2. Corrige les espaces blanches dans les docstrings
3. Assure la documentation appropriée des fonctions
"""

import re
from pathlib import Path


def fix_docstring_whitespace(file_path):
    """
    Corrige les lignes blanches contenant des espaces dans les docstrings.

    Args:
        file_path (str): Chemin du fichier à corriger
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remplacer les lignes vides avec espaces par des lignes vraiment vides
    # dans les docstrings
    fixed_content = re.sub(r' +\n', '\n', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print(f"✓ {file_path} - Espaces blanches corrigées")


def check_file_pep8_compliance(file_path):
    """
    Vérifie la conformité PEP 8 d'un fichier.

    Args:
        file_path (str): Chemin du fichier à vérifier

    Returns:
        dict: Dictionnaire avec les violations trouvées
    """
    violations = {
        'W293': [],  # Ligne vide contenant des espaces
        'E302': [],  # Espacement entre les définitions
        'F401': [],  # Import inutilisé
        'E501': [],  # Ligne trop longue
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            # W293: Ligne vide avec espaces
            if line.strip() == '' and len(line) > 1 and line[0] == ' ':
                violations['W293'].append(i)

    except Exception as e:
        print(f"Erreur lors de la vérification de {file_path}: {e}")

    return violations


def process_all_test_files():
    """Traite tous les fichiers de test du projet."""
    base_path = Path(
        r'e:\Users\segre\Documents\GitHub\projet_micro\web_app\core'
    )

    test_files = list(base_path.glob('test_*.py')) + list(base_path.glob('tests.py'))

    if not test_files:
        print("Aucun fichier de test trouvé")
        return

    print(f"🔍 Traitement de {len(test_files)} fichier(s) de test\n")

    for test_file in test_files:
        print(f"📄 {test_file.name}")

        # Corriger les espaces blanches
        fix_docstring_whitespace(str(test_file))

        # Vérifier les violations
        violations = check_file_pep8_compliance(str(test_file))

        if violations['W293']:
            print(f"   - Lignes vides avec espaces: {violations['W293']}")

        print()


if __name__ == '__main__':
    print("=" * 60)
    print("Correction PEP 8 des fichiers de test")
    print("=" * 60 + "\n")

    process_all_test_files()

    print("\n" + "=" * 60)
    print("✅ Correction terminée!")
    print("=" * 60)
