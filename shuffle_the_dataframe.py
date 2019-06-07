from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
dataset = shuffle(dataset)
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values
