import os
import shutil
from pathlib import Path

base_dir = Path("Sprites")

shiny_dir = base_dir / "shiny"
normal_dir = base_dir / "normal"
shiny_dir.mkdir(exist_ok=True)
normal_dir.mkdir(exist_ok=True)
uncategorized = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Skip files from target folders
        if "shiny" in Path(root).parts or "normal" in Path(root).parts:
            continue

        file_path = Path(root) / file

        # Checк file extension (image)
        if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            if "shiny" in file.lower():
                shutil.move(str(file_path), str(shiny_dir / file))
            elif "normal" in file.lower():
                shutil.move(str(file_path), str(normal_dir / file))
            else:
                uncategorized.append(str(file_path))

# Print paths of files that were not categorized
if uncategorized:
    print("Файлы, которые не были распределены:")
    for path in uncategorized:
        print(path)
else:
    print("Все файлы успешно распределены!")
