import sys
import os
import argparse

try:
    from Cython.Build import cythonize
except ImportError:
    print("Bibliothèque cython non trouvé.")
    sys.exit(1)

parser = argparse.ArgumentParser(description='Obfuscateur de fichier Python avec Cython.')
parser.add_argument('fichier', metavar='F', type=str, help='Le fichier à obfusquer.')
parser.add_argument('-o', '--output', type=str, help='Le nom du fichier obfusqué (par défaut : "obfusque_fichier.py").', default=None)

args = parser.parse_args()

nom_du_fichier_pk = args.fichier
if not os.path.exists(nom_du_fichier_pk):
    print("Le fichier %s n'existe pas." % nom_du_fichier_pk)
    sys.exit(1)

if args.output:
    nom_fichier_obfusque_srx = args.output
else:
    nom_fichier_obfusque_srx = "obfusque_" + nom_du_fichier_pk

cythonize(nom_du_fichier_pk, compiler_directives={'linetrace': False, 'binding': True},
          output_file=nom_fichier_obfusque_srx)
print("Le fichier %s a été obfusqué avec succès %s." % (nom_du_fichier_pk, nom_fichier_obfusque_srx))
