import numpy as np
arr = np.array([10,20,30,40,50])
arr[arr > 25] = 0
print("Updated array:", arr)