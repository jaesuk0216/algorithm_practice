A,B = [], []

N,M = map(int,input().split())

for row in range(N) :
    row = list(map(int,input().split()))
    A.append(row)

for row in range(N) :
    row = list(map(int,input().split()))
    B.append(row)

for row in range(N) :
    for cal in range(M) :
        print(A[row][cal] + B[row][cal], end = ' ')
    print()