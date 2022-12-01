num_list = list()

for i in range(5) :
    num = int(input())
    num_list.append(num)


num_list.sort()

print('{:.0f}'.format(sum(num_list)/5))
print(num_list[2])