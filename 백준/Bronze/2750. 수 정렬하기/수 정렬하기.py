num_set = set()

test = int(input())

for i in range(test) :
    num = int(input())
    num_set.add(num)

num_list = list(num_set)

num_list.sort()

for i in range(len(num_list)) :
    print(num_list[i])