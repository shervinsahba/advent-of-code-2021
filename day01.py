import numpy as np

depths = np.loadtxt('day01-input', dtype=int)
convolved_depths = np.convolve(depths, np.ones(3), 'valid')
answer = lambda x: (np.diff(x) > 0).sum()
print(answer(depths), answer(convolved_depths))