# Titanic EDA in VS Code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Check current directory and file
print("Current directory:", os.getcwd())
print("Files:", os.listdir())

# Load dataset
df = pd.read_csv("train.csv")
print("Dataset Loaded \n")

# Basic Info
print("Shape:", df.shape)
print("\nInfo:\n")
print(df.info())
print("\nDescribe:\n")
print(df.describe(include='all'))

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualizing missing data
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()

# Histograms
df.hist(figsize=(12, 10), bins=20)
plt.suptitle("Feature Distributions", fontsize=16)
plt.tight_layout()
plt.show()

# Boxplots
plt.figure(figsize=(10, 5))
sns.boxplot(x='Fare', data=df)
plt.title("Fare Boxplot")
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='Age', data=df)
plt.title("Age Boxplot")
plt.show()

# Categorical Analysis
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Class")
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Sex")
plt.show()

sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title("Survival by Embarked Port")
plt.show()

# Correlation Heatmap
df_corr = df.copy()
df_corr['Sex'] = df_corr['Sex'].map({'male': 0, 'female': 1})
df_corr['Embarked'] = df_corr['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

plt.figure(figsize=(10, 6))
numeric_df = df_corr.select_dtypes(include=[np.number])  # Keep only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)

plt.title("Correlation Heatmap")
plt.show()

# Age distribution by survival
sns.histplot(data=df, x="Age", hue="Survived", kde=True, bins=30)
plt.title("Age vs Survival")
plt.show()

# Fare vs Survival by Class
sns.boxplot(x='Pclass', y='Fare', hue='Survived', data=df)
plt.title("Fare vs Survival by Class")
plt.show()

# Handling missing values
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)
df.drop(columns=['Cabin'], inplace=True)

print("\n Missing values handled.")
