with open('input/day06') as f:
    data = list(map(int, f.read().split(',')))

counts = [data.count(timer) for timer in range(9)]

def total(c, days):
    for _ in range(days):
        c = c[1:] + [c[0]]
        c[6] += c[-1]
    return sum(c)

print(total(counts, 80), total(counts, 256))
