import numpy as np

res1 = np.array((1,1,1,1,1,1,1,1,1,1))
res2 = np.array([[2,2,2,2],[2,3,4,4]])

row_vector = np.array([1,2,3])
col_vector = np.array([[1],[2],[3] ])

print(np.dot(row_vector, col_vector))
print(row_vector @ col_vector)

print(row_vector[2:3])