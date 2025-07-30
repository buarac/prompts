import os
import shutil
import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("❌ Usage : python deplacer_capture.py <nom_fichier_destination>")
        sys.exit(1)

    nouveau_nom = sys.argv[1]
    desktop_path = Path.home() / "Desktop"
    fichiers_capture = list(desktop_path.glob("Capture*"))

    if len(fichiers_capture) == 0:
        print("❌ Aucun fichier commençant par 'Capture' trouvé sur le bureau.")
        sys.exit(1)

    if len(fichiers_capture) > 1:
        print("❌ Plusieurs fichiers 'Capture*' trouvés, opération annulée.")
        print("Fichiers détectés :")
        for f in fichiers_capture:
            print(f" - {f.name}")
        sys.exit(1)

    source = fichiers_capture[0]
    destination = Path.cwd() / nouveau_nom

    try:
        shutil.move(str(source), str(destination))
        print(f"✅ Fichier déplacé : {source.name} → {destination.name}")
    except Exception as e:
        print(f"❌ Erreur lors du déplacement : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()