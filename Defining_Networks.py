import numpy as np
import torch

import tools

import matplotlib.pyplot as plt
from torchvision import datasets, transforms


#Definir las transformadas para normalizar la data

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                ])

#Descargar y cargar la data de entrenamiento



