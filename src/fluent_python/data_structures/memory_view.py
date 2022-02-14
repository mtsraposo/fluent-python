import array

# build memoryview from array of 5 short signed integers (typecode 'h')
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)

# cast elements to typecode 'B' (unsigned char)
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# >>> [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

# assign value 4 to byte offset 5
memv_oct[5] = 4
print(numbers)
# >>> array('h', [-2, -1, 1024, 1, 2])
# Assigning 4 to the most significant byte of a 2-byte unsigned integer
# equals 4 * 2**8 = 1024.
# For 3, this would be 3 * 2**8 = 768
print(memv_oct.tolist())