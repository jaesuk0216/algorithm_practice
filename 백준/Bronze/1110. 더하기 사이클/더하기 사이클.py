first_num = int(input())
num = first_num
count = 0


while True :
    share_num = num // 10
    re_num = num % 10
    num = share_num + re_num  #몫 + 나머지
    se_num = num % 10
    num = (re_num *10) + se_num

    count +=1

    if first_num == num :
        break

print(count)