import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Variables
# fixed acidity - acids that don't readily evaporate
# volatile acidity - amount of acetic acid in wine (high levels lead to unpleasant, vinegar taste)
# citric acid - adds 'freshness' and flavor to wines
# residual sugar - the amount of sugar remaining after fermentation stops, it's rare to find wines with less than 1 gram/liter and wines with greater than 45 grams/liter are considered sweet
# chlorides - amount of salt in the wine
# free sulfur dioxide - the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion; it prevents microbial growth and the oxidation of wine
# total sulfur dioxide - amount of free and bound forms of SO2; in low concentrations, SO2 is mostly undetectable in wine, but at free SO2 concentrations over 50 ppm, SO2 becomes evident in the nose and taste of wine
# density - density of wine is close to water's density depending on alcohol and sugar content
# pH - how acidic and basic a wine is 
# sulphates - additive that can contribute to SO2, which act as antimicrobial and antioxidant
# alcohol - percent of alcohol content
# quality - output variable (0 - 10)

# Goal: Predict the quality of wine
# What variables create high quality wine?

# Read csv and put in data frame
wine_quality = pd.read_csv('winequality-red.csv')
print(wine_quality.head())

# Explore data
print(wine_quality.groupby(['quality']).mean()) # Data frame grouped by quality with averages
plt.figure(figsize = (8, 8))
sns.heatmap(wine_quality.corr(), annot = True)
plt.show()
