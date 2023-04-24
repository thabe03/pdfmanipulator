import os
import subprocess



# Arguments de la commande OCRmyPDF
arguments = ["ocrmypdf", "--skip-text", chemin_fichier, chemin_sortie]

# Exécuter la commande OCRmyPDF
subprocess.run(arguments)

# Vérifier si le fichier de sortie a été créé
if os.path.exists(chemin_sortie):
    print("OCR terminée. Fichier de sortie :", {0}_subset.pdf)
else:
    print("Erreur : impossible de créer le fichier de sortie")

def ocr(chemin_fichier):
