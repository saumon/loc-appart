#!/usr/bin/env python3
"""
Script pour regénérer des thumbnails de haute qualité
Redimensionne les images originales pour créer des thumbnails plus grandes et moins pixélisées
"""

import os
import sys
from PIL import Image, ImageOps
import shutil

def create_high_quality_thumbnails():
    """Créer des thumbnails de haute qualité"""
    
    # Chemins
    photos_dir = "photos"
    thumbnails_dir = "photos/thumbnails"
    
    # Taille des thumbnails (largeur max)
    THUMBNAIL_WIDTH = 600
    THUMBNAIL_HEIGHT = 400
    
    # Qualité JPEG (0-100)
    JPEG_QUALITY = 85
    
    print("🔄 Régénération des thumbnails en cours...")
    print(f"📏 Nouvelle taille: {THUMBNAIL_WIDTH}x{THUMBNAIL_HEIGHT} max")
    print(f"🎨 Qualité JPEG: {JPEG_QUALITY}%")
    print()
    
    # Créer le dossier thumbnails s'il n'existe pas
    os.makedirs(thumbnails_dir, exist_ok=True)
    
    # Lister toutes les images dans le dossier photos
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
    images = []
    
    for filename in os.listdir(photos_dir):
        if os.path.isfile(os.path.join(photos_dir, filename)):
            _, ext = os.path.splitext(filename.lower())
            if ext in image_extensions:
                images.append(filename)
    
    if not images:
        print("❌ Aucune image trouvée dans le dossier photos/")
        return
    
    print(f"📸 {len(images)} images trouvées")
    print()
    
    success_count = 0
    error_count = 0
    
    for i, filename in enumerate(images, 1):
        try:
            input_path = os.path.join(photos_dir, filename)
            output_path = os.path.join(thumbnails_dir, filename)
            
            print(f"[{i:2d}/{len(images)}] {filename:<35}", end=" ")
            
            # Ouvrir l'image originale
            with Image.open(input_path) as img:
                # Obtenir les dimensions originales
                original_width, original_height = img.size
                
                # Calculer les nouvelles dimensions en gardant le ratio
                if original_width > original_height:
                    # Image paysage
                    new_width = THUMBNAIL_WIDTH
                    new_height = int((original_height * THUMBNAIL_WIDTH) / original_width)
                else:
                    # Image portrait
                    new_height = THUMBNAIL_HEIGHT
                    new_width = int((original_width * THUMBNAIL_HEIGHT) / original_height)
                
                # Redimensionner avec un algorithme de haute qualité
                thumbnail = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Appliquer l'orientation EXIF si nécessaire
                thumbnail = ImageOps.exif_transpose(thumbnail)
                
                # Sauvegarder avec optimisation
                if filename.lower().endswith(('.jpg', '.jpeg')):
                    thumbnail.save(output_path, 'JPEG', 
                                 quality=JPEG_QUALITY, 
                                 optimize=True, 
                                 progressive=True)
                else:
                    # Convertir en JPEG pour uniformiser
                    output_path = os.path.splitext(output_path)[0] + '.jpg'
                    if thumbnail.mode in ('RGBA', 'LA', 'P'):
                        # Créer un fond blanc pour les images avec transparence
                        background = Image.new('RGB', thumbnail.size, (255, 255, 255))
                        if thumbnail.mode == 'P':
                            thumbnail = thumbnail.convert('RGBA')
                        background.paste(thumbnail, mask=thumbnail.split()[-1] if thumbnail.mode in ('RGBA', 'LA') else None)
                        thumbnail = background
                    
                    thumbnail.save(output_path, 'JPEG', 
                                 quality=JPEG_QUALITY, 
                                 optimize=True, 
                                 progressive=True)
                
                # Afficher les infos
                file_size = os.path.getsize(output_path) / 1024  # en KB
                print(f"✅ {new_width}x{new_height} ({file_size:.0f}KB)")
                success_count += 1
                
        except Exception as e:
            print(f"❌ Erreur: {str(e)}")
            error_count += 1
    
    print()
    print("=" * 60)
    print(f"📊 Résumé:")
    print(f"   ✅ Succès: {success_count}")
    print(f"   ❌ Erreurs: {error_count}")
    print(f"   📁 Dossier: {thumbnails_dir}")
    print()
    
    if success_count > 0:
        print("🎉 Thumbnails regénérés avec succès!")
        print("💡 Les nouvelles thumbnails sont de meilleure qualité et moins pixélisées.")
        print("🌐 Votre galerie photo aura maintenant des images plus nettes!")
    else:
        print("⚠️  Aucun thumbnail n'a pu être créé.")

if __name__ == "__main__":
    try:
        create_high_quality_thumbnails()
    except KeyboardInterrupt:
        print("\n\n⏹️  Opération annulée par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {str(e)}")
        sys.exit(1)
