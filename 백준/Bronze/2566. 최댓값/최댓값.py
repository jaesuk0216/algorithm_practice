num = []
max_val = 0
col = 0
row = 0

for i in range(9) :
    num = list(map(int,input().split()))
    if max(num) > max_val :
        max_val = max(num)
        col = i
        row = num.index(max_val)

print(max_val)
print(col+1, row+1)