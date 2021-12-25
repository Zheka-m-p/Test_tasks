import sys

a = []
with open(sys.argv[1]) as inf:
    for line in inf:
        line = line.strip()
        a.append(line)
A = [int(i) for i in a]

count = 0
m = sorted(A)[len(A) // 2]
print(sum(abs(j - m) for j in A))
