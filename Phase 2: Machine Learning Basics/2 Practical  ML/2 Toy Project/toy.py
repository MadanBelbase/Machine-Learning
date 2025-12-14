# -*- coding: utf-8 -*-
# Toy.py
# VS Code compatible version

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (update path if needed)
df = pd.read_csv("DataSet/placement.csv")

# Basic inspection
print(df.head())
print(df.info())

# Remove first column (likely index/serial number)
df = df.iloc[:, 1:]
print(df.head())

# Scatter plot
plt.scatter(df['cgpa'], df['iq'], c=df['placement'])
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("CGPA vs IQ")
plt.show()

# Features and target
x = df.iloc[:, 0:2]
y = df.iloc[:, -1]

print(x.shape)
print(y.shape)

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.1, random_state=42
)

# Feature scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Logistic Regression model
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Accuracy
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Decision boundary plot
from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, y_train.values, clf=clf, legend=2)
plt.xlabel("CGPA (scaled)")
plt.ylabel("IQ (scaled)")
plt.title("Decision Boundary")
plt.show()
