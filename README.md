# Titanic EDA Analysis 🛳️

This repository contains an in-depth **Exploratory Data Analysis (EDA)** of the famous [Titanic dataset](https://www.kaggle.com/competitions/titanic/data). The goal is to understand the data, detect patterns, visualize relationships, and handle missing or noisy data.

---

## 📁 Files Included

| File               | Description                                         |
|--------------------|-----------------------------------------------------|
| `train.csv`        | Titanic dataset used for analysis (from Kaggle)     |
| `titanic_eda.py`   | Python script performing full EDA                   |
| `plots/` (optional)| Folder containing saved visualizations (if added)   |

---

## 📊 Key EDA Tasks Performed

✅ Data Overview  
✅ Handling Missing Values  
✅ Univariate Analysis  
✅ Bivariate Analysis  
✅ Outlier Detection  
✅ Correlation Heatmap  
✅ Visual Insights using `matplotlib` and `seaborn`

---

## 🔍 Visualizations

- 🔥 Heatmap of missing values
- 📦 Boxplots of `Fare` and `Age` (to spot outliers)
- 📈 Histograms of numerical columns
- 👥 Countplots by `Sex`, `Pclass`, `Embarked`, and `Survived`
- 🌡️ Correlation Heatmap (only numerical features)

---

## 📦 Requirements

```bash
pip install pandas matplotlib seaborn
