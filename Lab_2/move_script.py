import os
import shutil
from pathlib import Path

# Пути
source_dir = Path("data/electro_guitars")
train_dir = Path("data/music_dataset/train/electro_guitars")
val_dir = Path("data/music_dataset/val/electro_guitars")  
test_dir = Path("data/music_dataset/test/electro_guitars")

# Создаем папки
for dir in [train_dir, val_dir, test_dir]:
    dir.mkdir(parents=True, exist_ok=True)

files = sorted(source_dir.glob("guitar_*.png"))

# Разбиваем: первые 65 в train, следующие 15 в val, остальные в test
train_files = files[:65]
val_files = files[65:80]
test_files = files[80:100]

for file in train_files:
    shutil.move(str(file), str(train_dir / file.name))

for file in val_files:
    shutil.move(str(file), str(val_dir / file.name))
    
for file in test_files:
    shutil.move(str(file), str(test_dir / file.name))

print(f"Перемещено: {len(train_files)} в train, {len(val_files)} в val, {len(test_files)} в test")