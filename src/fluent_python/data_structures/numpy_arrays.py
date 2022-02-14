import numpy as np
from random import random
import os

from time import perf_counter as pc

resources_path = 'src/fluent_python/data_structures/resources'
file_path = os.path.join(resources_path, 'floats-10M-lines.txt')

# Create file with 10 million floats line by line
floats_list = [random() for i in range(10 ** 7)]
os.mkdir('src/fluent_python/data_structures/resources')
fp = open(file_path, 'w')
ROW_FORMAT = '{:.4f}\n'
[fp.write(ROW_FORMAT.format(floats_list[i])) for i in range(10 ** 7)]
fp.close()

# Load file into a Numpy Array, carry out elementwise operations
# and save a memory-mapped file into another array; this allows efficient
# processing of slices of the array even if it does not fit entirely in memory.
floats = np.loadtxt('src/fluent_python/data_structures/resources/floats-10M-lines.txt')
floats *= .5
t0 = pc()
floats /= 3
print(pc() - t0)  # 0.007242833999953291
np.save(os.path.join(resources_path, 'floats–10M.npy'), 'r+')

# Remove files, because they are heavy (>70MB)
os.remove(os.path.join(resources_path, 'floats–10M.npy'))
os.remove(os.path.join(resources_path, 'floats-10M-lines.txt'))
