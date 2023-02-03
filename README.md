# Obfuscateur Python avec Cython

Petit script qui permet d'obfusquer des fichiers Python en utilisant Cython (en C).

## Prérequis

- Python 3
- Cython ( ``pip install cython`` )

## Utilisation

``python obf.py obfusque_fichier.py``

Pour obfusquer le fichier mon_fichier.py en utilisant un nom de fichier obfusqué personnalisé :

``python obf.py obfusque_fichier.py -o mon_nom.py``

Le fichier obfusqué sera enregistré sous le nom spécifié.

## Note

L'obfuscation de code n'offre pas une sécurité à 100%, mais peut aider à masquer le code source de vos projets Python.
