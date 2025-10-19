import os
import shutil
from pathlib import Path
import random

# Set random seed for reproducibility
random.seed(42)

def train_test_split(data, train_size=0.7, random_state=42):
    """Simple train-test split implementation"""
    random.seed(random_state)
    data = list(data)
    random.shuffle(data)
    split_idx = int(len(data) * train_size)
    return data[:split_idx], data[split_idx:]

first_class_name = 'normal'
second_class_name = 'shiny'
# Define paths
base_dir = Path('Sprites')
first_class_dir = base_dir / first_class_name
second_class_dir = base_dir / second_class_name

# Create output directories
output_dir = base_dir / 'dataset'
for split in ['train', 'val', 'test']:
    for class_name in [first_class_name, second_class_name]:
        (output_dir / split / class_name).mkdir(parents=True, exist_ok=True)

# Get all image files
first_class_images = [f for f in first_class_dir.iterdir() if f.suffix.lower() in ['.jpg', '.png', '.jpeg']]
second_class_images = [f for f in second_class_dir.iterdir() if f.suffix.lower() in ['.jpg', '.png', '.jpeg']]

print(f"Found {len(first_class_images)} {first_class_name} images")
print(f"Found {len(second_class_images)} {second_class_name} images")

# Function to split and copy images
def split_and_copy(images, class_name, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    # First split: train vs (val+test)
    train_images, temp_images = train_test_split(images, train_size=train_ratio, random_state=42)

    # Second split: val vs test
    val_images, test_images = train_test_split(temp_images, train_size=val_ratio/(val_ratio+test_ratio), random_state=42)

    # Copy files
    for img in train_images:
        shutil.copy2(img, output_dir / 'train' / class_name / img.name)

    for img in val_images:
        shutil.copy2(img, output_dir / 'val' / class_name / img.name)

    for img in test_images:
        shutil.copy2(img, output_dir / 'test' / class_name / img.name)

    print(f"{class_name}: {len(train_images)} train, {len(val_images)} val, {len(test_images)} test")

# Split and copy images for both classes
split_and_copy(first_class_images, first_class_name)
split_and_copy(second_class_images, second_class_name)