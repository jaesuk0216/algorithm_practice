a = input()
year = int(a)
count = 0

if year % 4 == 0 and year % 100 !=0 :
    count +=1
elif year % 400 == 0 and year % 100 == 0 and year % 400 ==0 :
    count +=1

print(count)