import numpy as np

with open('input/day05') as f:
    data = [line.split('->')[i].strip().split(',') 
        for line in f.readlines() for i in [0,1]]
    data = np.array(data, int).reshape(-1,4)

def chart(data, diagonals=True):
    grid = np.zeros((np.max(data)+1, np.max(data)+1), int)
    for x1,y1,x2,y2 in data:
        if x1 == x2:
            grid[min(y1,y2):max(y1,y2)+1, x1] += 1
        elif y1 == y2:
            grid[y1, min(x1,x2):max(x1,x2)+1] += 1
        elif diagonals:
            for x,y in  zip(range(x1,x2+1) if x2>x1 else range(x2,x1+1)[::-1],
                            range(y1,y2+1) if y2>y1 else range(y2,y1+1)[::-1]):
                grid[y, x] += 1
    return grid

answer = lambda x: np.count_nonzero(x >= 2)

print(answer(chart(data, diagonals=False)), 
      answer(chart(data, diagonals=True)))
