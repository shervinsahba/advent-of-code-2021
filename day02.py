import numpy as np

def answer1(directions, position = np.array([0,0])):
    unit_vectors = {x: np.array(y) for x,y in zip(['forward', 'up', 'down'], [[1,0], [0,-1], [0,1]])}

    for name, val in zip(directions[::2], directions[1::2]):
        position += int(val) * unit_vectors[name]
    
    return position


def answer2(directions, position = np.array([0,0,0])):
    unit_vectors = {x: np.array(y) for x,y in zip(['forward', 'up', 'down'], [[1,1,0], [0,0,-1], [0,0,1]])}

    for name, val in zip(directions[::2], directions[1::2]):
        position += int(val) * np.array([1, position[2], 1]) * unit_vectors[name]
    
    return position


if __name__ == '__main__':

    with open('day02-input') as f:
        directions = list(filter(None, f.read().split()))

    print(np.multiply(*answer1(directions)))
    print(np.multiply(*answer2(directions)[:2]))