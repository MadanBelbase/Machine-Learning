# Curse of Dimensionality

when we add or have more features, the accuracy of the model may decrease instead of increase due to the curse of dimensionality.After  a certain point, adding more features can lead to overfitting,the model becomes too complex and starts to memorize the training data instead of generalizing to new data. This can result in poor performance on unseen data.

 <!-- where the model accuracy  is decreased. This is called curse of dimensionality -->

  

# PCA (Principal Component Analysis)
PCA stands for principal  component analysis. It is a dimensionality reduction technique that is often used to reduce the number of features in a dataset while retaining as much variance as possible. PCA works by identifying the directions (principal components) in which the data varies the most and projecting the data onto these directions.

Benefits of PCA:
1. Dimensionality Reduction: PCA helps to reduce the number of features in a dataset, which can lead to faster training times and reduced computational costs.2
2. Visualization: PCA can be used to visualize high-dimensional data in a lower-dimensional space (e.g., 2D or 3D), making it easier to understand and interpret.

Example scenario:
Suppose we have a dataset with 100 features, and we want to reduce it to 2 dimensions for visualization purposes. We can use PCA to identify the two principal components that capture the most variance in the data and project the data onto these components.

