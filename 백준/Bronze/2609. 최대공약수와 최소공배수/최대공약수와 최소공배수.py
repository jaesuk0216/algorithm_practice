a,b = map(int,input().split())
A,B =a,b

while b != 0 :
    a = a%b
    a,b = b,a

print(a)
print(A*B//a)
