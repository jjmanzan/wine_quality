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

## Correlation heatmap
plt.figure(figsize = (8, 8))
sns.heatmap(wine_quality.corr(), annot = True)
plt.show()

## Scatterplots of input variables vs output variable
plt.figure(figsize = (15, 10))

plt.subplot(4, 3, 1)
sns.regplot(data = wine_quality, x = 'fixed acidity', y = 'quality')
plt.title('Fixed Acidity vs Quality')
plt.xlabel('Fixed Acidity')
plt.ylabel('Quality')

plt.subplot(4, 3, 2)
sns.regplot(data = wine_quality, x = 'volatile acidity', y = 'quality')
plt.title('Volatile Acidity vs Quality')
plt.xlabel('Volatile Acidity')
plt.ylabel('Quality')

plt.subplot(4, 3, 3)
sns.regplot(data = wine_quality, x = 'citric acid', y = 'quality')
plt.title('Citric Acid vs Quality')
plt.xlabel('Citric Acid')
plt.ylabel('Quality')

plt.subplot(4, 3, 4)
sns.regplot(data = wine_quality, x = 'residual sugar', y = 'quality')
plt.title('Residual Sugar vs Quality')
plt.xlabel('Residual Sugar')
plt.ylabel('Quality')

plt.subplot(4, 3, 5)
sns.regplot(data = wine_quality, x = 'chlorides', y = 'quality')
plt.title('Chlorides vs Quality')
plt.xlabel('Chlorides')
plt.ylabel('Quality')

plt.subplot(4, 3, 6)
sns.regplot(data = wine_quality, x = 'free sulfur dioxide', y = 'quality')
plt.title('Free Sulfur Dioxide vs Quality')
plt.xlabel('Free Sulfur Dioxide')
plt.ylabel('Quality')

plt.subplot(4, 3, 7)
sns.regplot(data = wine_quality, x = 'total sulfur dioxide', y = 'quality')
plt.title('Total Sulfur Dioxide vs Quality')
plt.xlabel('Total Sulfur Dioxide')
plt.ylabel('Quality')

plt.subplot(4, 3, 8)
sns.regplot(data = wine_quality, x = 'density', y = 'quality')
plt.title('Density vs Quality')
plt.xlabel('Density')
plt.ylabel('Quality')

plt.subplot(4, 3, 9)
sns.regplot(data = wine_quality, x = 'pH', y = 'quality')
plt.title('pH vs Quality')
plt.xlabel('pH')
plt.ylabel('Quality')

plt.subplot(4, 3, 10)
sns.regplot(data = wine_quality, x = 'sulphates', y = 'quality')
plt.title('Sulphates vs Quality')
plt.xlabel('Sulphates')
plt.ylabel('Quality')

plt.subplot(4, 3, 11)
sns.regplot(data = wine_quality, x = 'alcohol', y = 'quality')
plt.title('Alcohol vs Quality')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
