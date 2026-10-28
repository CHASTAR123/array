import numpy as np
linear_array = np.array([2, 4, 6])
print(linear_array + linear_array)
print(linear_array * 3)
print(linear_array + 5)
print(np.sum(linear_array))
print(np.min(linear_array))
print(np.max(linear_array))
print(np.mean(linear_array))
print(np.std(linear_array))
print(linear_array.shape)
print(linear_array.ndim)
print(linear_array.size)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
# print(l1 / 2)
print(sum(l1 + l2))