import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

train_data = pd.read_csv('./data/train.csv')
test_data = pd.read_csv('./data/test.csv')

train_data[1:10]