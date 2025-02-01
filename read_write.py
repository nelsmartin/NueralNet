import numpy as np

array = np.zeros((2, 2))
f = open("pysource2.txt", "r")
for i in range((len(array))):
        for j in range(len(array[i])):
            array[i][j] = (f.readline())

print(array)