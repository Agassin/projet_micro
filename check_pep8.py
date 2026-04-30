#!/usr/bin/env python
"""
Flake8 Linter Helper Script
Facilite l'exécution de Flake8 pour vérifier la conformité PEP 8
"""

import subprocess
import sys
from pathlib import Path

def run_flake8(args=None):
    """Exécute Flake8 avec les arguments fournis."""
    if args is None:
        args = ['web_app/']
    
    cmd = [sys.executable, '-m', 'flake8'] + args
    
    print(f"Exécution: {' '.join(cmd)}\n")
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("\n✅ Aucune erreur PEP 8 détectée !")
    else:
        print(f"\n❌ {result.returncode} erreur(s) PEP 8 trouvée(s)")
    
    return result.returncode

if __name__ == '__main__':
    # Vérifier que flake8 est installé
    try:
        import flake8
    except ImportError:
        print("❌ Erreur: Flake8 n'est pas installé")
        print("Installez-le avec: pip install flake8")
        print("Ou: pip install -r requirements-dev.txt")
        sys.exit(1)
    
    # Passer tous les arguments en ligne de commande à flake8
    exit_code = run_flake8(sys.argv[1:] if len(sys.argv) > 1 else ['web_app/'])
    sys.exit(exit_code)
