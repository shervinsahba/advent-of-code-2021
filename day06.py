with open('input/day06') as f:
    data = list(map(int, f.read().split(',')))
    
data = [data.count(timer) for timer in range(9)]

total = []
for _ in range(256):    
    data.append(data[0])
    data = [x for x in data[1:]]
    data[6] += data[-1]

    total.append(sum(data))
   
print(total[79], total[255])
