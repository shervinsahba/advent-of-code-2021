import numpy as np

depths = np.loadtxt('input/day01', dtype=int)
convolved_depths = np.convolve(depths, np.ones(3), 'valid')
answer = lambda x: (np.diff(x) > 0).sum()
print(answer(depths), answer(convolved_depths))