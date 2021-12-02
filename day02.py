import numpy as np

unit_vectors = {x: np.array(y) for x,y in zip(['forward', 'up', 'down'], [[1,0], [0,-1], [0,1]])}

with open('day02-input') as f:
    directions = list(filter(None, f.read().split()))

position = np.array([0,0])
for name, val in zip(directions[::2], directions[1::2]):
    position += int(val) * unit_vectors[name]

print(position[0] * position[1])