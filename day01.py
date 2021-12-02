import numpy as np

def main():
    depths = np.loadtxt('day01-data', dtype=int)
    convolved_depths = np.convolve(depths, np.ones(3), 'valid')
    answer = lambda x: (np.diff(x) > 0).sum()
    print(answer(depths), answer(convolved_depths))


if __name__ == '__main__':
    main()