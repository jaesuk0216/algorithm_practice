x_num = []
y_num = []

for _ in range(3) :
    x,y = map(int,input().split())
    x_num.append(x)
    y_num.append(y)

for i in range(3) :
    if x_num.count(x_num[i]) == 1 :
        x_ = x_num[i]

    if y_num.count(y_num[i]) == 1 :
        y_ = y_num[i]

print(x_,y_)