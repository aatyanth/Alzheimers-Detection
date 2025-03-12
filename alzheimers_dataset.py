import torch
from torch.utils.data import Dataset
from torchvision.io import read_image

class alzheimers_dataset(Dataset):
    
    def __init__(self, df, transform=None):
        self.df = df
        self.transform = transform
        
    def __len__(self):
        return len(self.df['class_label'])
    
    def __getitem__(self, index):
        image_path = self.df['image_path'].iloc[index]
        image = read_image(image_path)
        label = self.df['class_label'].iloc[index]
        if self.transform:
            image = self.transform(image)
        
        return image, label