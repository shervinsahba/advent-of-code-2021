import numpy as np


def bingo(boards, calls):
    boards_ = np.copy(boards)
    winners, scores = [], []
    for call in calls:
        for n, board in enumerate(boards_):
            if n not in winners and call in board:
                r, c = np.where(board == call)
                board[r, c] = -1
                if (board[r,:] < 0).all() or (board[:,c] < 0).all():
                    scores += [board[board > 0].sum() * call]
                    winners += [n]
    return list(zip(winners, scores))


if __name__ == '__main__':
    with open('input/day04') as f:
        calls, *boards = f.read().split('\n')

    calls = np.array(calls.split(','), int)
    boards = np.loadtxt(boards, int).reshape(-1,5,5)
    results = bingo(boards, calls)

    print(results[0], results[-1])
