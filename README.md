# Shiny Pokemon Classification

A deep learning project for classifying Pokemon images as normal or shiny variants using transfer learning with PyTorch.

## Project Overview

This project implements a binary image classifier to distinguish between normal and shiny Pokemon. Three different pre-trained models are tested:
- **ResNet152** - Test Accuracy: 59.64%
- **Vision Transformer (ViT)** - Test Accuracy: 60.36%
- **Swin Transformer** - Test Accuracy: 60.36%

## Dataset

The dataset is organized into three splits:
- **Train**: 1,274 samples
- **Validation**: 273 samples
- **Test**: 275 samples

Classes: `normal` and `shiny`

## Features

- Transfer learning using pre-trained models (ResNet152, ViT, Swin Transformer)
- Data augmentation for training (rotation, flipping, color jitter)
- Learning rate scheduling with ReduceLROnPlateau
- Training visualization (loss and accuracy plots)
- Prediction with probability outputs

## Model Architecture

Each model uses transfer learning:
- Base model weights are frozen
- Custom classification head is added:
  - Linear layer (model_features → 256)
  - ReLU activation
  - Dropout (0.3)
  - Linear layer (256 → 2 classes)

## Training Parameters

- Batch size: 32
- Epochs: 50
- Learning rate: 0.01
- Optimizer: Adam
- Loss function: CrossEntropyLoss
- Scheduler: ReduceLROnPlateau

## Results

The best performing models (ViT and Swin) achieved ~60% accuracy on the test set, suggesting this is a challenging classification task due to subtle visual differences between normal and shiny Pokemon variants.
