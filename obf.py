import sys
import os
import argparse

try:
    from Cython.Build import cythonize
except ImportError:
    print("Vous devez installer la bibliothèque cython pour utiliser ce script.")
    sys.exit(1)

parser = argparse.ArgumentParser(description='Obfuscateur de fichier Python avec Cython.')
parser.add_argument('fichier', metavar='F', type=str, help='Le fichier à obfusquer.')
parser.add_argument('-o', '--output', type=str, help='Le nom du fichier obfusqué (par défaut, le nom sera "obfusque_fichier.py").', default=None)

args = parser.parse_args()

nom_du_fichier = args.fichier
if not os.path.exists(nom_du_fichier):
    print("Le fichier %s n'existe pas." % nom_du_fichier)
    sys.exit(1)

if args.output:
    nom_fichier_obfusque = args.output
else:
    nom_fichier_obfusque = "obfusque_" + nom_du_fichier

cythonize(nom_du_fichier, compiler_directives={'linetrace': False, 'binding': True},
          output_file=nom_fichier_obfusque)
print("Le fichier %s a été obfusqué avec succès %s." % (nom_du_fichier, nom_fichier_obfusque))
