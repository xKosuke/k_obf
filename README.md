# Obfuscateur Python avec Cython

Ce script permet d'obfusquer des fichiers Python en utilisant la bibliothèque Cython (en C). Il peut être utilisé pour protéger le code source de vos projets Python.

## Prérequis

- Python 3
- Cython ( ``pip install cython`` )

## Utilisation

``python obf.py nom_du_fichier.py``

Pour obfusquer le fichier mon_fichier.py en utilisant un nom de fichier obfusqué personnalisé :

``python obf.py nom_du_fichier.py -o nom_du_fichier_obf.py``

Le fichier obfusqué sera enregistré sous le nom spécifié.

## Note

L'obfuscation de code n'offre pas une sécurité à 100%, mais peut aider à masquer le code source de vos projets Python.
