import json
import uuid
import argparse
from datetime import datetime
from pathlib import Path
import sys

def format_datetime():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def process_file(input_path, output_path):
    # Charger le JSON
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier d'entrée : {e}")
        sys.exit(1)

    if not isinstance(data, list):
        print("Le fichier JSON doit contenir une liste d'éléments.")
        sys.exit(1)

    total = len(data)
    updated = 0

    for item in data:
        if isinstance(item, dict) and "id" in item:
            item["id"] = str(uuid.uuid4())
            updated += 1
        if "updatedAt" in item:
            item["updatedAt"] = format_datetime()

    # Sauvegarder le fichier mis à jour
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier de sortie : {e}")
        sys.exit(1)

    print(f"\n✅ Traitement terminé.")
    print(f"Nombre d’éléments traités : {total}")
    print(f"Nombre d’UUID mis à jour : {updated}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Met à jour les champs 'id' avec un UUID et 'updatedAt' avec la date courante.")
    parser.add_argument("-i", "--input", required=True, help="Chemin du fichier JSON d’entrée")
    parser.add_argument("-o", "--output", required=True, help="Chemin du fichier JSON de sortie")
    
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.is_file():
        print(f"Fichier d’entrée introuvable : {input_path}")
        sys.exit(1)

    process_file(input_path, output_path)