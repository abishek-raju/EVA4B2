import os
import numpy as np
from torchvision import datasets

from tensornet.data.datasets.dataset import BaseDataset


class CIFAR10(BaseDataset):
    """Load CIFAR-10 Dataset."""
    
    def _download(self, train=True, apply_transform=True):
        """Download dataset.

        Args:
            train (bool, optional): True for training data.
                (default: True)
            apply_transform (bool, optional): True if transform
                is to be applied on the dataset. (default: True)
        
        Returns:
            Downloaded dataset.
        """
        transform = None
        if apply_transform:
            transform = self.train_transform if train else self.val_transform
        return datasets.CIFAR10(
            self.path, train=train, download=True, transform=transform
        )

    def _get_image_size(self):
        """Return shape of data i.e. image size."""
        return np.transpose(self.sample_data.data[0], (2, 0, 1)).shape
    
    def _get_classes(self):
        """Return list of classes in the dataset."""
        return (
            'plane', 'car', 'bird', 'cat', 'deer',
            'dog', 'frog', 'horse', 'ship', 'truck'
        )
    
    def _get_mean(self):
        """Returns mean of the entire dataset."""
        return tuple(np.mean(self.sample_data.data, axis=(0, 1, 2)) / 255)
    
    def _get_std(self):
        """Returns standard deviation of the entire dataset."""
        return tuple(np.std(self.sample_data.data, axis=(0, 1, 2)) / 255)
