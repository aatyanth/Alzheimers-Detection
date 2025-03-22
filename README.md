# Evaluating Deep Learning Models for Early Alzheimer’s Detection in Magnetic Resonance Imaging

## Overview

This project compares the performance of three deep learning architectures (CNN, ResNet, and Vision Transformer) for early detection of Alzheimer's Disease using MRI images.
- ***Full report, titled "Evaluating_Deep_Learning_Models_for_Early_Alzheimer's_Detection_in_Magnetic_Resonance_Imaging.pdf" is attached in the repo above***

## Dataset

- Source: OASIS-1 dataset
- Contents: MRI scans of 416 subjects aged 18-96
- Preprocessing: Converted to 2D jpg files by splicing 3D brain scans


## Classification Tasks

1. Binary: No Alzheimer's vs. Alzheimer's
2. Multiclass: No Alzheimer's, Mild Alzheimer's, Advanced Alzheimer's

## Models Evaluated

1. Baseline CNN
2. ResNet-18 (modified)
3. Vision Transformer (ViT)

## Key Results

| Model | Test Accuracy |
| :-- | :-- |
| CNN | 45% ± 5.0% |
| ResNet | 70% ± 5.0% |
| ViT | 55% ± 5.0% |

- ResNet outperformed both the baseline CNN and Vision Transformer
- ViT performance was likely limited by the relatively small dataset size


## Conclusions

- ResNet showed superior performance in capturing complex spatial relationships in MRI images
- Deep learning approaches show promise for early Alzheimer's detection
- Further optimization could potentially improve model performance


## Future Work

- Expand dataset size
- Fine-tune model hyperparameters further
- Explore hybrid architectures combining multiple data modalities


## Acknowledgments

Data were provided [in part] by OASIS-1: Cross-Sectional: Principal Investigators: D. Marcus, R, Buckner, J, Csernansky J. Morris; P50 AG05681, P01 AG03991, P01 AG026276, R01 AG021910, P20 MH071616, U24 RR021382

The processed dataset containing the 2D images were provided by Ninad Aithal: https://www.kaggle.com/datasets/ninadaithal/imagesoasis/data
