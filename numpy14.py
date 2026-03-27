import numpy as np

def main():
    print("=== NumPy Program Demo ===\n")

    # 1. Creating arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("1D Array:", arr1)
    print("2D Array:\n", arr2)
    # 2. Array properties
    print("\nShape of arr2:", arr2.shape)
    print("Data type:", arr1.dtype)
    # 3. Zeros and Ones
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    print("\nZeros array:\n", zeros)
    print("Ones array:\n", ones)
    # 4. Arithmetic operations
    print("\nAddition:", arr1 + 2)
    print("Multiplication:", arr1 * 3)
    # 5. Mathematical functions
    print("\nSquare root:", np.sqrt(arr1))
    print("Exponential:", np.exp(arr1))
    # 6. Statistical operations
    print("\nMean:", np.mean(arr1))
    print("Sum:", np.sum(arr1))
    print("Max:", np.max(arr1))
    print("Min:", np.min(arr1))
    # 7. Reshaping arrays
    reshaped = arr1.reshape((5, 1))
    print("\nReshaped array:\n", reshaped)
    # 8. Indexing and slicing
    print("\nFirst element:", arr1[0])
    print("Slice (1 to 3):", arr1[1:4])
    # 9. Random numbers
    random_arr = np.random.rand(3, 3)
    print("\nRandom array:\n", random_arr)
main()