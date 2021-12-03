import numpy as np

with open('day02-input') as f:
    directions = list(filter(None, f.read().split()))

vectors = dict(zip(['forward', 'up', 'down'], map(np.array, [[1, 1, 0], [0, 0, -1], [0, 0, 1]])))

position1, position2 = [0,0,0], [0,0,0]  # [horizontal, n/a, depth], [horizontal, depth, aim]
for name, val in zip(directions[::2], directions[1::2]):
    position1 += int(val) * vectors[name]
    position2 += int(val) * np.array([1, position2[2], 1]) * vectors[name]

print(position1[0]*position1[2])
print(position2[0]*position2[1])

