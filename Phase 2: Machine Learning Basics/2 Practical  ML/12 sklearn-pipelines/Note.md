# Scikit-learn Pipelines

## Definition

A Pipeline in scikit-learn chains together multiple steps so that the output of one step is automatically used as the input for the next step.

## Purpose

* Makes it easy to apply the same preprocessing to both training and testing data.
* Helps prevent errors like data leakage and column mismatches.
* Simplifies workflow by combining preprocessing and model training in one single object.

## How it Works

1. Data enters the first step of the pipeline (e.g., imputation, scaling, encoding).
2. The transformed data flows to the next step automatically.
3. The final step is usually a model, which produces the output/predictions.

### Diagram (simplified flow):

```
Input → Step 1 → Step 2 → Step 3 → Output
```

* Each block represents a transformation or model.
* Output of one block = input to the next.



