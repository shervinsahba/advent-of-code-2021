import numpy as np

data = np.loadtxt('input/day07', int, delimiter=',')

# 1. brute force solutions.
gas = min(np.abs(data - x).sum() for x in range(np.max(data)))

cost = lambda s: s*(s+1)/2  # sum of values 1 to s
gas2 = min(cost(np.abs(data-x)).sum() for x in range(np.max(data)))

print(gas, gas2)


# 2. more elegant solutions using properties of the system.

# in part 1, the cost is the L1 norm. median minimizes it.
gas = np.abs(data - np.median(data)).sum()

# in part 2, the cost is given by sum of 1 to s, which is also the average of the L2 and L1 norms.
# Minimizing the cost gives s = mean(x) - 1/2 * mean(sgn(x-s)), which is ugly.
# But we're working with integers, so we know s is within an integer of mean(x).
xb = np.round(np.mean(data)) + np.array([-1,0,1])
gas2 = min(cost(np.abs(data - x)).sum() for x in xb)

print(gas, gas2)
