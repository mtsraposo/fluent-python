import os
from random import random
import pickle

import time
from array import array


def print_run_time(command):
    start = time.time()
    exec(command)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    # <<< ARRAYS >>>
    floats_array = array('d', (random() for i in range(10 ** 7)))
    fp = open('floats.bin', 'wb')

    array_to_file_builtin = "floats_array.tofile(fp)"
    print_run_time(array_to_file_builtin)  # 0.022664785385131836

    array_to_file_pickle = "pickle.dump(floats_array, fp)"
    print_run_time(array_to_file_pickle)  # 0.0980980396270752

    fp.close()

    # <<< LISTS >>>
    floats_list = [random() for i in range(10 ** 7)]
    fp = open('floats.bin', 'w')

    ROW_FORMAT = '%s\n'
    list_to_file = "[fp.write(ROW_FORMAT.format(floats_list[i])) for i in range(10 ** 7)]"
    print_run_time(list_to_file)  # 1.4601781368255615

    fp.close()
    os.remove('floats.bin')
    # Bottom line === the array builtin .tofile is much faster than dumping lists to files
