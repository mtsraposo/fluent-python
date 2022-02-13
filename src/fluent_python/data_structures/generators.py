colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# The generator expression yields items one by one; a list with
# all six T-shirt variations is never produced in this example,
# which saves memory when the lists are very large
for tshirt in (f'({c}, {s})' for c in colors for s in sizes):
    print(tshirt)
