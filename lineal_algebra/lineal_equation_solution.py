# use numpy to get solution
from scipy import linalg
import numpy

augmented_matrices = numpy.array([[1, -2, 0, 3], [0, 1, 0, -4], [0, 0, 1, 0], [0, 0, 0, 1]])
lineal_res = numpy.array([-2, 7, 6, -3])

solutions = linalg.solve(augmented_matrices, lineal_res)
print(solutions)

