import torch
from torch.utils.data import Dataset
import torchvision
from torchvision.io import read_image
from PIL import Image
import torchvision.transforms as tf
import os
import numpy as np
import pandas as pd

class alzheimers_dataset(Dataset):
    
    def __init__(self, root_dir, image_paths, labels, transform=None):
        self.root_dir = root_dir
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform
        
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, index):
        image_path = self.root_dir + self.image_paths[index]
        image = Image.open(image_path).convert('L')
        label = self.labels[index]
        if self.transform:
            image = self.transform(image)
        
        return image, label