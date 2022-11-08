test_case = int(input())

for i in range(test_case) :
    num,code = input().split()
    num = int(num)

    for j in range(len(code)) :
        print(num*code[j], end = '')
    print()