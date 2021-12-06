with open('input/day06') as f:
    data = list(map(int, f.read().split(',')))

data = [data.count(timer) for timer in range(9)]

def tally(data, days):
    for _ in range(days):
        data = data[1:] + [data[0]]
        data[6] += data[-1]
    return sum(data)

print(tally(data, 80), tally(data, 256))
