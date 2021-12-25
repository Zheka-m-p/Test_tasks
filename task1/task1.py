import sys

a = []
with open(sys.argv[1]) as inf:
    for line in inf:
        line = line.strip().split()
        a.extend(line)
A = [int(i) for i in a]

i = 1
result = []
while True:
    result.append(i)
    i = 1 + (i + A[1] - 2) % A[0]
    if i == 1:
        break
        
print(*result, sep='')
