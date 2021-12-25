import sys
a = []
with open(sys.argv[1]) as inf:
    for line in inf:
        line = line.strip().split()
        a.extend(line)
A = [float(i) for i in a]
b= []
with open(sys.argv[2]) as inf:
    for line in inf:
        line= line.strip().split()
        b.extend(line)
B = [float(i) for i in b]
for i in range(0, len(B), 2):
    if ((A[0] - B[i])**2 + (A[1] - B[i + 1])**2) ** 0.5 == A[2]:
        print('0')
    elif ((A[0] - B[i])**2 + (A[1] - B[i + 1])**2) ** 0.5 < A[2]:
        print('1')
    elif ((A[0] - B[i])**2 + (A[1] - B[i + 1])**2) ** 0.5 > A[2]:
        print('2')
