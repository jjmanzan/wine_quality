import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Goal: Predict the quality of wine
# What variables create high quality wine?

wine_quality = pd.read_csv('winequality-red.csv')
df = pd.DataFrame(data = wine_quality)

print(df.info())