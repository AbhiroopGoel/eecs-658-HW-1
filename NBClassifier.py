"""
EECS 658 Assignment 1
Program: NBClassifier.py

Description:
Implements a Gaussian Naive Bayes classifier on the Iris dataset
using 2-fold cross-validation. Outputs accuracy, confusion matrix,
precision, recall, and F1 scores.

Inputs:
iris.csv dataset 
*Already provided in lecture modules 

Outputs:
- Overall accuracy
- Confusion matrix
- Precision, Recall, F1 for each Iris class

Author: Abhiroop Goel
Creation Date: 22nd January 2026
Sources:
- EECS 658 Supervised Learning slides
- Assignment 1 instructions
- ChatGpt
- Stackoverflow 
- github
"""

""" Here use import the libraries that we need to initialize the GaussianNB, and then used sklearn module to access our matrrics and formulas"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
dataset = pd.read_csv(
    "iris.csv",
    names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
)

# Separate features and labels (we separate both using iloc to split the string and then get the values)
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

# 2-fold split (50% / 50%)
X_fold1, X_fold2, y_fold1, y_fold2 = train_test_split(
    X, y, test_size=0.50, random_state=1
)

# Initialize model
model = GaussianNB()

# Fold 1: Train on Fold1, Test on Fold2
model.fit(X_fold1, y_fold1)
pred1 = model.predict(X_fold2)

# Fold 2: Train on Fold2, Test on Fold1
model.fit(X_fold2, y_fold2)
pred2 = model.predict(X_fold1)

# Combine results
actual = np.concatenate((y_fold2, y_fold1))
predicted = np.concatenate((pred1, pred2))

# Output results
print("Accuracy:", accuracy_score(actual, predicted))
print("\nConfusion Matrix:\n", confusion_matrix(actual, predicted))
print("\nClassification Report:\n", classification_report(actual, predicted))
