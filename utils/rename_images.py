import os
from pathlib import Path

# Définition des nouveaux noms
image_mapping = {
    "compressed-piclumen-1733912444603.webp": "ramonage-cheminee-lille.webp",
    "compressed-piclumen-1733912505192.webp": "insert-cheminee-moderne.webp",
    "compressed-piclumen-1733912507709.webp": "cheminee-traditionnelle-nord.webp",
    "compressed-piclumen-1733912509474.webp": "renovation-cheminee-lille.webp",
    "compressed-piclumen-1733912511045.webp": "foyer-ouvert-cheminee.webp",
    "compressed-piclumen-1733912571861.webp": "cheminee-contemporaine-design.webp",
    "compressed-piclumen-1733912575613.webp": "entretien-cheminee-metropole.webp",
    "compressed-piclumen-1733912577945.webp": "conduit-cheminee-inspection.webp",
    "compressed-piclumen-1733912581668.webp": "cheminee-pierre-renovation.webp",
    "compressed-piclumen-1733912768741.webp": "installation-insert-cheminee.webp",
    "compressed-piclumen-1733912896300.webp": "cheminee-brique-restauration.webp",
    "compressed-piclumen-1733912997919.webp": "tubage-cheminee-professionnel.webp",
    "compressed-piclumen-1733913004213.webp": "securite-cheminee-verification.webp",
    "compressed-piclumen-1733913011367.webp": "cheminee-ancienne-restauree.webp"
}

def rename_images():
    # Chemin vers le dossier des images
    image_dir = Path(__file__).parent.parent / 'public' / 'images'
    
    # Vérifier que le dossier existe
    if not image_dir.exists():
        print(f"Le dossier {image_dir} n'existe pas!")
        return
    
    # Renommer chaque image
    for old_name, new_name in image_mapping.items():
        old_path = image_dir / old_name
        new_path = image_dir / new_name
        
        if old_path.exists():
            try:
                old_path.rename(new_path)
                print(f"Renommé: {old_name} -> {new_name}")
            except Exception as e:
                print(f"Erreur lors du renommage de {old_name}: {str(e)}")
        else:
            print(f"Le fichier {old_name} n'existe pas")

if __name__ == "__main__":
    rename_images()
