from collections import deque

#  Deques are optimized to append and end from the ends

dq = deque(range(10), maxlen=10)
dq.rotate(3)
dq.rotate(-4)
dq.appendleft(-1)
dq.extend([11, 22, 33])
dq.extendleft([10, 20, 30, 40])
print(dq)
# >>> deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
