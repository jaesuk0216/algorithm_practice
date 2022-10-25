num = []
for i in range(9) :
    num.append(int(input()))
k = max(num)
print(k)
print(num.index(k)+1)