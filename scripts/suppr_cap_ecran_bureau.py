import os
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Supprime les fichiers PNG 'Capture*.png' du bureau.")
    parser.add_argument("-v", action="store_true", help="Affiche les fichiers supprimés (mode verbeux)")
    args = parser.parse_args()

    desktop = Path.home() / "Desktop"
    count = 0

    for file in desktop.iterdir():
        if (
            file.is_file()
            and file.name.startswith("Capture")
            and file.suffix.lower() == ".png"
        ):
            try:
                file.unlink()
                count += 1
                if args.v:
                    print(f"Supprimé : {file.name}")
            except Exception as e:
                print(f"Erreur lors de la suppression de {file.name} : {e}")

    print(f"\nTotal supprimé : {count} fichier(s)")

if __name__ == "__main__":
    main()