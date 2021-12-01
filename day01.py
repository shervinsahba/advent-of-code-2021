import numpy as np

def main():
    with open('day01-data') as f:
        depths = np.array(list(filter(None, f.read().split('\n'))), dtype=int)

    answer1 = sum(depths[:-1] < depths[1:])

    convolved_depths = np.convolve(depths, np.ones(3), 'valid')

    answer2 = sum(convolved_depths[:-1] < convolved_depths[1:])

    print(answer1, answer2)


if __name__ == '__main__':
    main()