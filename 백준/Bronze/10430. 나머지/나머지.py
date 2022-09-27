num1, num2, num3 = input().split()
a = int(num1)
b = int(num2)
c = int(num3)

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)