#!/usr/bin/env python3
"""Convert heaviest webp images to AVIF for ~40% bandwidth saving."""
from pathlib import Path
from PIL import Image
import pillow_avif  # noqa: F401  (registers AVIF codec)
import os

ROOT = Path("/home/user/workspace/winnersclub.com")
IMG_DIR = ROOT / "images"

THRESHOLD_BYTES = 80_000  # convert anything over 80KB

converted = 0
saved_bytes = 0
for img_path in IMG_DIR.glob("*.webp"):
    avif_path = img_path.with_suffix(".avif")
    if avif_path.exists():
        continue
    src_bytes = img_path.stat().st_size
    if src_bytes < THRESHOLD_BYTES:
        continue
    try:
        with Image.open(img_path) as im:
            im.save(avif_path, format="AVIF", quality=55, speed=6)
        new_bytes = avif_path.stat().st_size
        saved = src_bytes - new_bytes
        if saved > 0:
            saved_bytes += saved
            converted += 1
            print(f"  {img_path.name}: {src_bytes//1024}KB → {new_bytes//1024}KB ({saved*100//src_bytes}% saved)")
        else:
            # AVIF was bigger, delete it
            avif_path.unlink()
    except Exception as e:
        print(f"  ERR {img_path.name}: {e}")

print(f"\nConverted {converted} images, total saved: {saved_bytes//1024}KB")
