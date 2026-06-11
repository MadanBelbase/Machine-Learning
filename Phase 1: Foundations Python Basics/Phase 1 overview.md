# Phase 1: Foundations — Python Basics

> Build the core Python and data science toolkit needed before diving into Machine Learning.

---

## Overview

Phase 1 establishes your programming foundation. You'll go from basic Python syntax all the way through scientific computing libraries (NumPy, Pandas, Matplotlib) and essential programming skills like file handling and modules. Every topic here directly supports the data manipulation and analysis work you'll do in ML.

---

## Curriculum Breakdown

### 🐍 Python Core (Lessons 1–7)

| Lesson | Focus |
|---|---|
| Python 1 | Syntax basics — variables, data types, operators |
| Python 2 | Control flow — if/else, loops (for, while) |
| Python 3 | Functions — defining, calling, scope, return values |
| Python 4 | Data structures — lists, tuples, sets, dictionaries |
| Python 5 | Object-Oriented Programming — classes, objects, inheritance |
| Python 6 | Error handling — try/except, exceptions, debugging |
| Python 7 | Review — consolidate and practice everything so far |

---

### 🔢 NumPy (Lessons 8–9)

NumPy is the backbone of numerical computing in Python. Nearly every ML library is built on top of it.

| Lesson | Focus |
|---|---|
| Python 8 | NumPy arrays, creation, operations (add, multiply, reshape) |
| Python 9 | Indexing, slicing, broadcasting — accessing and manipulating array data efficiently |

**Key concepts to master:**
- `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
- Array shapes and reshaping
- Broadcasting rules (operating on arrays of different shapes)
- Vectorized operations (avoid Python loops — use NumPy)

---

### 🐼 Pandas (Lessons 10–12)

Pandas is the primary tool for working with real-world datasets — loading, cleaning, and transforming tabular data.

| Lesson | Focus |
|---|---|
| Python 10 | Pandas Series & DataFrames — creating, reading, basic operations |
| Python 11 | Data Cleaning & Missing Values — `dropna`, `fillna`, handling nulls |
| Python 12 | GroupBy, Merge, Pivot Tables — aggregation and joining datasets |

**Key concepts to master:**
- Loading data: `pd.read_csv()`, `pd.read_excel()`
- Selecting data: `df['col']`, `df.loc[]`, `df.iloc[]`
- Handling missing data: `isnull()`, `fillna()`, `dropna()`
- Grouping: `groupby().agg()`
- Merging: `pd.merge()`, `concat()`

---

### 📊 Data Visualization (Lesson 13)

| Lesson | Focus |
|---|---|
| Python 13 | Matplotlib + Seaborn — plotting charts, distributions, heatmaps |

**Chart types to know:**
- Line plot → trends over time
- Bar chart → categorical comparisons
- Histogram → distribution of values
- Scatter plot → relationships between variables
- Heatmap → correlation matrices (critical for ML feature analysis)
- Box plot → outlier detection

---

### 🗂️ File Handling & Modules (Lessons 14–15)

| Lesson | Focus |
|---|---|
| Python 14 | File handling — read/write `.txt`, `.csv`, `.json` files |
| Python 15 | Modules — importing, creating custom modules, using `pip` packages |

**Key concepts:**
- `open()`, `read()`, `write()`, `with` statement
- Working with `os`, `sys`, `json`, `csv` standard library modules
- Installing packages with `pip install`
- Creating reusable `.py` modules

---

## Skills You'll Have After Phase 1

- Write clean, structured Python code
- Work with arrays and matrices using NumPy
- Load, clean, and transform datasets with Pandas
- Visualize data distributions and relationships
- Handle files and organize code into reusable modules

---

## Recommended Practice

- **Kaggle Learn** — Free Python and Pandas micro-courses
- **LeetCode Easy (Python)** — Strengthen core Python logic
- **Practice Dataset** — Download the Titanic or Iris dataset and explore it fully using only Pandas and Matplotlib before moving to Phase 2