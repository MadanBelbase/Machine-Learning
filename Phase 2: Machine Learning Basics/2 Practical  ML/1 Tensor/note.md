### Tensor
tensor are multi-dimensional arrays that are used to represent data in machine learning and deep learning. They are a generalization of matrices to higher dimensions and can be thought of as containers for data that can be processed by machine learning algorithms.

Tensors can have different ranks, which indicate the number of dimensions they have. For example:
- A scalar (single value) is a rank-0 tensor.
- A vector (1D array) is a rank-1 tensor.
- A matrix (2D array) is a rank-2 tensor.
- A 3D array is a rank-3 tensor, and so on.

Tensors are commonly used in deep learning frameworks such as TensorFlow and PyTorch, where they serve as the primary data structure for storing and manipulating data during model training and inference. They support various operations such as addition, multiplication, reshaping, and slicing, which are essential for building and training machine learning models.

Rank of Tensor:
- Rank 0: Scalar (e.g., 5)
- Rank 1: Vector (e.g., [1, 2, 3])
- Rank 2: Matrix (e.g., [[1, 2], [3, 4]])
- Rank 3: 3D Tensor (e.g., [[[1], [2]], [[3], [4]]])
- Rank n: n-dimensional array
Tensors are essential for representing complex data structures in machine learning, such as images, audio, and text, enabling efficient computation and manipulation of data during the training and evaluation of models.

Axis of Tensor:
The axis of a tensor refers to the dimensions along which operations can be performed. Each axis corresponds to a specific dimension of the tensor. For example, in a 2D tensor (matrix), there are two axes:
- Axis 0: Represents the rows of the matrix.
- Axis 1: Represents the columns of the matrix.
In higher-dimensional tensors, additional axes represent additional dimensions. For example, in a 3D tensor, there would be three axes:
- Axis 0: Represents the depth (or layers) of the tensor.
- Axis 1: Represents the rows.
- Axis 2: Represents the columns.
Understanding the axes of a tensor is crucial for performing operations such as slicing, reshaping, and aggregating data along specific dimensions. For instance, when summing a tensor along a particular axis, the operation will collapse that dimension, resulting in a tensor with one less dimension.
 