a,b,c = input().split()
num1 = int(a)
num2 = int(b)
num3 = int(c)

if num1 == num2 == num3 :
    print(10000 + (num1*1000))

elif num1 == num2 :
    print(1000 + (num1 * 100))

elif num1 == num3 :
    print(1000 + (num1 * 100))

elif num2 == num3 :
    print(1000 + (num2 * 100))

else :
    if num1 > num2 :
        if num1 > num3 :
            print(num1 *100)
    if num2 > num1 :
        if num2 > num3 :
            print(num2 * 100)
    if num3 > num2 :
        if num3 > num1 :
            print(num3 * 100)