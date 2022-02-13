# <<< Mutable vs. Immutable Objects >>>

# Mutable: the augmented assignment, the __iadd__ is implemented and the
# change occurs in place
l = [1, 2, 3]
print(id(l))  # 4697121408
l *= 2
print(l)
print(id(l))  # 4697121408

# Immutable: the change creates a new object
t = (1, 2, 3)
print(id(t))  # 4694154240
t *= 2
print(id(t))  # 4696957280

# Bottom line === Repeated concatenation of immutable sequences is inefficient.


# <<< Tuple Riddle >>>
import dis

t = (1, 2, [30, 40])
t[2] += [50, 60]  # Throws TypeError: 'tuple' object does not support item assignment
# Get bytecode for expression
dis.dis('s[a] += b')
# Bottom line === Putting mutable items in tuples is not a good idea.



