num_1 = input()
num_2 = input()

first_num = int(num_1)
second_num = int(num_2)

num_100 = second_num // 100
num_10 = (second_num // 10)- 10*num_100
num = second_num - (100*num_100+10*num_10)

print(first_num*num)
print(first_num*num_10)
print(first_num*num_100)
print(first_num*second_num)