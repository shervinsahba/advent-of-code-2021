import numpy as np

def main():
    depths = np.loadtxt('day01-data', dtype=int)
    answer1 = sum(depths[:-1] < depths[1:])

    convolved_depths = np.convolve(depths, np.ones(3), 'valid')
    answer2 = sum(convolved_depths[:-1] < convolved_depths[1:])

    print(answer1, answer2)


if __name__ == '__main__':
    main()